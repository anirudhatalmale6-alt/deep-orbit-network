# -*- coding: utf-8 -*-
"""
Verification du site, dans un navigateur reel.

    python3 -m http.server 8875 --bind 127.0.0.1   # depuis la racine
    python3 tests/verif.py http://127.0.0.1:8875/

Lire la source dit ce qui a ete ecrit ; mesurer le rendu dit ce que le
navigateur a fait. Les contrastes, les debordements, les ancres, les
requetes reseau et le comportement du formulaire sont donc mesures dans un
Chromium reel, jamais deduits de la feuille de style.
"""

import html
import os
import re
import sys
import urllib.request

from playwright.sync_api import sync_playwright

_ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(_ICI)
sys.path.insert(0, os.path.join(RACINE, "source"))

import contenu as C  # noqa: E402

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8875/"
if not BASE.endswith("/"):
    BASE += "/"

_ok = [0]
_ko = []


def v(cond, nom):
    if cond:
        _ok[0] += 1
    else:
        _ko.append(nom)


def section(nom):
    print("\n== %s" % nom)


# Les largeurs encadrent CHAQUE point de bascule de la feuille de style
# (620, 800, 960, 1060). Une regle qui ne se trompe qu'a l'interieur d'une
# bande etroite ne peut donc pas se cacher entre deux mesures.
LARGEURS = [320, 360, 390, 414, 480, 600, 619, 621, 768, 799, 801, 899,
            959, 961, 1024, 1059, 1061, 1180, 1280, 1366, 1440]

# Seuls ces neuf fichiers peuvent apparaitre dans un <img>. C'est un
# allowlist, pas une recherche de mots interdits : une photographie ne peut
# pas entrer sans faire echouer ce controle, quel que soit son nom.
IMAGES_PERMISES = {"marque-accent.svg", "marque-clair.svg",
                   "marque-sombre.svg", "marque-duo.svg", "favicon.svg",
                   "tuile.svg", "frise.svg", "schema.svg", "legende.svg"}

# Les mots d'attente des AUTRES chantiers du meme client. Ils ne doivent
# jamais servir d'etiquette ici : six vocabulaires melanges ne sont plus un
# vocabulaire.
AUTRES_ATTENTES = ("à vérifier", "à définir", "To be decided",
                   "En attente d'autorisation", "À confirmer",
                   "To be confirmed", "À fixer", "To be set")

# Les marqueurs de negation sont cherches en MOTS ENTIERS.
#
# La premiere version les cherchait en sous-chaines, et « ne » se trouvait
# dans « Ligne éditoriale ». Le libelle du menu suffisait donc a faire
# passer n'importe quelle phrase de la page pour une negation. C'est ainsi
# qu'une mutation qui ecrivait « Notre fonds finance déjà des sociétés »
# n'a produit aucun echec.
NEGATIONS = re.compile(
    r"\b(?:aucun|aucune|aucuns|aucunes|ne|n'|ni|jamais|sans|"
    r"no|not|never|nothing|none|nor)\b", re.I)

# EXCEPTIONS RELUES A LA MAIN.
#
# Une liste d'exceptions est une dette : chaque ligne desarme le controle
# sur un fragment precis, et une liste qui s'allonge finit par tout
# autoriser. Elle est donc courte, exacte, et chaque entree porte sa
# raison. Un motif interdit n'est ignore que si la phrase ou il apparait
# contient l'un de ces fragments EXACTS.
EXCEPTIONS = [
    # Le mot « rendement » comme DECLENCHEUR DE RELECTURE, pas comme
    # promesse : c'est la liste de ce que la moderation doit examiner.
    "levée, valorisation, rendement",
    "fundraising, valuation, returns",
    # « 20 articles » est un OBJECTIF de son chapitre 13, pas un nombre
    # d'articles publies. Les deux pages qui le citent disent d'ailleurs
    # dans la meme phrase qu'ils ne sont pas ecrits.
    "20 premiers articles",
    "first 20 articles",
    # La phrase qui dit que ces 20 articles NE SONT PAS ecrits. Le motif
    # « un chiffre de frequentation » est volontairement sans exception de
    # negation — un nombre de membres reste interdit meme nie — donc cette
    # phrase-ci doit etre nommee explicitement.
    "20 articles ne sont pas écrits",
    "20 articles are not written",
]

# Motifs interdits. Ceux marques `dur=True` sont interdits sans exception ;
# les autres sont tolerés dans une phrase NEGATIVE, parce que c'est
# exactement ainsi qu'on ecrit un avertissement (« aucun rendement ne sera
# publie »), et qu'interdire le mot interdirait l'avertissement.
INTERDITS = [
    # --- chiffres et dates : jamais, sous aucune forme
    (r"\b\d{1,3}\s?%", "un pourcentage", True),
    (r"\b(19|20)\d{2}\b", "une annee", True),
    (r"\b\d{1,3}\s?(?:M|k|K)?(?:€|\$|USD|EUR)\b", "un montant", True),
    (r"(?:€|\$)\s?\d", "un montant", True),
    (r"\+\d[\d\s().-]{7,}", "un numero de telephone", True),
    (r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "une adresse mail",
     True),
    (r"\b\d+\s*(?:membres|members|abonnés|subscribers|articles|"
     r"startups|projets|projects)\b", "un chiffre de frequentation", True),
    # --- organisations reelles : ce site n'a aucun lien avec elles
    (r"\b(NASA|ESA|SpaceX|Blue Origin|Arianespace|Roscosmos|ISRO|JAXA|"
     r"CNES|Rocket Lab|Boeing|Airbus|Starlink|Falcon 9|Starship|Ariane)\b",
     "une organisation ou un produit reel", True),
    # --- promesses financieres : tolerees uniquement en phrase negative
    (r"\brendement", "un rendement", False),
    (r"\breturns?\b", "un rendement", False),
    (r"\bperformance", "une performance", False),
    (r"\bgarant(?:i|ie|is|ies)\b", "une garantie", False),
    (r"\bguarantee", "une garantie", False),
    (r"\bconseil en investissement", "un conseil en investissement", False),
    (r"\binvestment advice", "un conseil en investissement", False),
    (r"\bnotre fonds\b", "un fonds presente comme existant", False),
    (r"\bour fund\b", "un fonds presente comme existant", False),
    # --- superlatifs et sensationnalisme (chapitre 11)
    (r"\ble meilleur\b|\bla meilleure\b|\bthe best\b", "un superlatif",
     False),
    (r"\brévolutionnaire\b|\brevolutionary\b", "un superlatif", False),
    (r"\bunique au monde\b|\bworld leader\b|\bleader mondial\b",
     "un superlatif", False),
    (r"\bpreuve que\b|\bproof that\b", "une preuve annoncee", False),
    (r"\bnous avons découvert\b|\bwe have discovered\b", "une decouverte",
     False),
]


def lire(url):
    with urllib.request.urlopen(url) as r:
        return r.read().decode("utf-8")


def toutes_pages():
    for p in C.PAGES:
        yield "fr", p, "fr/" + p[0]
        yield "en", p, "en/" + p[1]


def phrases(texte):
    return re.split(r"(?<=[.!?:;])\s+|\n", texte)


# =========================================================== 1. structure
def s_structure(sources):
    section("1. structure des pages")
    for lang, p, rel in toutes_pages():
        s = sources[rel]
        n = rel
        v(s.startswith("<!doctype html>"), "%s : doctype" % n)
        v('<html lang="%s">' % lang in s, "%s : lang" % n)
        v(s.count("<h1") == 1, "%s : un seul h1" % n)
        v('class="evitement"' in s, "%s : lien d'evitement" % n)
        v('rel="canonical"' in s, "%s : canonique" % n)
        v(s.count('rel="alternate"') == 3, "%s : trois hreflang" % n)
        v('content="noindex,nofollow"' in s, "%s : noindex" % n)
        v('rel="icon"' in s, "%s : favicon" % n)
        m = re.search(r'name="description" content="([^"]*)"', s)
        v(m is not None, "%s : description presente" % n)
        if m:
            v(40 <= len(m.group(1)) <= 175,
              "%s : longueur de description (%d)"
              % (n, len(m.group(1)) if m else 0))
        # aucun outil de mesure, aucune donnee structuree
        for mot in ("google-analytics", "gtag(", "googletagmanager",
                    "application/ld+json", "facebook.net", "hotjar",
                    "matomo", "plausible"):
            v(mot not in s, "%s : pas de %s" % (n, mot))
        # le nom est marque comme provisoire
        v(s.count('class="prov"') >= 2,
          "%s : nom marque provisoire au moins deux fois" % n)
        # la convention est enoncee sur chaque page
        v('class="convention"' in s, "%s : la convention est enoncee" % n)


# ====================================================== 2. images et tiers
def s_images(sources):
    section("2. images permises et aucune ressource tierce")
    for lang, p, rel in toutes_pages():
        s = sources[rel]
        for src in re.findall(r'<img[^>]+src="([^"]+)"', s):
            base = src.split("/")[-1].split("?")[0]
            v(base in IMAGES_PERMISES,
              "%s : image permise (%s)" % (rel, base))
        for url in re.findall(r'(?:src|href)="(https?://[^"]+)"', s):
            v(url.startswith(BASE) or "anirudhatalmale6-alt.github.io" in url,
              "%s : aucune ressource tierce (%s)" % (rel, url[:48]))
        v("googleapis" not in s and "cdn." not in s,
          "%s : aucun CDN" % rel)


# ========================================================== 3. interdits
def s_interdits(sources):
    section("3. les motifs interdits")
    for lang, p, rel in toutes_pages():
        s = sources[rel]
        texte = re.sub(r"<script.*?</script>", " ", s, flags=re.S)
        # Chaque fin de bloc devient une fin de phrase.
        #
        # Sans cela, le menu, le fil d'Ariane et le titre se collent en une
        # seule « phrase » de trois cents caracteres, parce que rien de
        # tout cela ne se termine par un point. La fenetre examinee autour
        # d'un motif interdit avalait alors la moitie de l'en-tete, et il
        # suffisait qu'un libelle de menu contienne un marqueur de negation
        # pour innocenter la phrase suivante.
        texte = re.sub(r"</(?:p|li|h[1-6]|div|section|article|td|th|nav|"
                       r"header|footer|figcaption|label|option|button|a)>",
                       " . ", texte)
        texte = re.sub(r"<[^>]+>", " ", texte)
        texte = texte.replace("&nbsp;", " ").replace("&#8239;", " ")
        texte = re.sub(r"\s+", " ", texte)
        for motif, nom, dur in INTERDITS:
            trouves = []
            for m in re.finditer(motif, texte, re.I):
                deb = texte.rfind(".", 0, m.start()) + 1
                fin = texte.find(".", m.end())
                ph = texte[deb:fin if fin > 0 else len(texte)]
                if any(x in ph for x in EXCEPTIONS):
                    continue
                if dur:
                    trouves.append(m.group(0))
                    continue
                # phrase negative ? alors c'est un avertissement, pas une
                # affirmation, et c'est precisement ce qu'on veut lire.
                if not NEGATIONS.search(ph):
                    trouves.append(m.group(0))
            v(not trouves, "%s : %s (%s)" % (rel, nom, trouves[:2]))


# ============================================== 4. vocabulaire d'attente
def s_attente(sources):
    section("4. le mot d'attente")
    for lang, p, rel in toutes_pages():
        s = sources[rel]
        for autre in AUTRES_ATTENTES:
            v(autre not in s,
              "%s : le mot d'attente d'un autre chantier (%s)"
              % (rel, autre))
    # il existe, et il est celui de ce chantier
    for lang, idx in (("fr", 0), ("en", 1)):
        cible = "fr/mentions-legales.html" if lang == "fr" \
            else "en/legal-notice.html"
        v(C.ATTENTE[idx] in sources[cible],
          "%s : le mot d'attente de ce chantier" % cible)


# ================================================== 5. statuts chapitre 11
def s_statuts(sources):
    section("5. les statuts du chapitre 11")
    for lang, idx in (("fr", 0), ("en", 1)):
        myst = "fr/mysteres-de-l-univers.html" if lang == "fr" \
            else "en/mysteries-of-the-universe.html"
        led = "fr/ligne-editoriale.html" if lang == "fr" \
            else "en/editorial-standards.html"
        s = sources[myst]
        # chaque item porte une etiquette
        n_items = s.count('class="item"')
        n_statuts = len(re.findall(r'class="statut statut-', s))
        v(n_items > 0, "%s : des items" % myst)
        v(n_items == n_statuts,
          "%s : un statut par item (%d items, %d statuts)"
          % (myst, n_items, n_statuts))
        # l'etiquette est du TEXTE, pas une couleur
        for cle in ("fait", "hypothese"):
            nom = C.STATUTS[cle][0][idx]
            v(nom in s, "%s : le mot « %s » est ecrit" % (myst, nom))
        # les quatre statuts sont definis sur la page ligne editoriale
        d = sources[led]
        for cle in ("fait", "hypothese", "opinion", "speculation"):
            nom, definition = C.STATUTS[cle]
            v(nom[idx] in d, "%s : « %s » defini" % (led, nom[idx]))
            # La page est du HTML echappe : `html.escape` transforme aussi
            # l'apostrophe en `&#x27;`. Comparer la chaine brute faisait
            # echouer les deux seules definitions qui en contiennent une,
            # et le controle accusait la page au lieu de lui-meme.
            v(html.escape(definition[idx][:38]) in d,
              "%s : definition de « %s »" % (led, nom[idx]))


# ================================================== 6. liens et plan de site
def s_liens(sources):
    section("6. liens, aller-retour de langue, plan de site")
    connus = set()
    for lang, p, rel in toutes_pages():
        connus.add(rel)
    for lang, p, rel in toutes_pages():
        s = sources[rel]
        dossier = rel.split("/")[0]
        for href in re.findall(r'href="([^"#?]+)"', s):
            if href.startswith("http") or href.startswith("mailto"):
                continue
            if href.startswith("../"):
                cible = href[3:]
                if cible.startswith("assets/"):
                    continue
            else:
                cible = dossier + "/" + href
            v(cible in connus or cible.startswith("assets/"),
              "%s : lien mort (%s)" % (rel, href))
    # aller-retour de langue
    for p in C.PAGES:
        fr = sources["fr/" + p[0]]
        en = sources["en/" + p[1]]
        v('href="../en/%s"' % p[1] in fr, "fr/%s -> en" % p[0])
        v('href="../fr/%s"' % p[0] in en, "en/%s -> fr" % p[1])
    sm = lire(BASE + "sitemap.xml")
    for p in C.PAGES:
        for lang in ("fr", "en"):
            f = p[0] if lang == "fr" else p[1]
            v("%s%s/%s" % (BASE, lang, f) in sm or lang + "/" + f in sm,
              "sitemap : %s/%s" % (lang, f))
    rb = lire(BASE + "robots.txt")
    v("Disallow: /" in rb, "robots.txt ferme en demonstration")


# ================================================================ 7. rendu
def s_rendu(pg):
    section("7. rendu : erreurs, requetes, debordement")
    for lang, p, rel in toutes_pages():
        erreurs = []
        externes = []
        pg.once("pageerror", lambda e: erreurs.append(str(e)))

        def _req(r):
            if not r.url.startswith(BASE) and not r.url.startswith("data:"):
                externes.append(r.url)
        pg.on("request", _req)
        pg.set_viewport_size({"width": 1280, "height": 800})
        pg.goto(BASE + rel, wait_until="networkidle")
        pg.remove_listener("request", _req)
        v(not erreurs, "%s : aucune erreur JS (%s)" % (rel, erreurs[:1]))
        v(not externes,
          "%s : aucune requete hors domaine (%s)" % (rel, externes[:1]))
        casse = pg.evaluate(
            "()=>[...document.images].filter(i=>!i.complete||"
            "i.naturalWidth===0).map(i=>i.src)")
        v(not casse, "%s : aucune image cassee (%s)" % (rel, casse[:1]))
        # hierarchie des titres : jamais de saut de niveau
        niveaux = pg.evaluate(
            "()=>[...document.querySelectorAll('h1,h2,h3,h4')]"
            ".map(h=>+h.tagName[1])")
        saut = [i for i in range(1, len(niveaux))
                if niveaux[i] - niveaux[i - 1] > 1]
        v(not saut, "%s : hierarchie des titres" % rel)


def s_debordement(pg):
    section("7b. aucun debordement horizontal")
    echantillon = ["fr/index.html", "fr/mysteres-de-l-univers.html",
                   "fr/startups-et-investissement.html",
                   "fr/feuille-de-route.html", "fr/contact.html",
                   "en/index.html", "en/startups-and-investment.html",
                   "en/roadmap.html"]
    for rel in echantillon:
        for w in LARGEURS:
            pg.set_viewport_size({"width": w, "height": 800})
            pg.goto(BASE + rel, wait_until="domcontentloaded")
            pg.wait_for_timeout(60)
            trop = pg.evaluate(
                "()=>document.documentElement.scrollWidth - "
                "document.documentElement.clientWidth")
            v(trop <= 1, "%s @%d : pas de debordement (%s px)"
              % (rel, w, trop))


# ============================================================== 8. ancres
def s_ancres(pg):
    section("8. ancres sous l'en-tete collant")
    for w in (390, 1280):
        pg.set_viewport_size({"width": w, "height": 780})
        pg.goto(BASE + "fr/contact.html", wait_until="networkidle")
        marge = pg.evaluate(
            "()=>getComputedStyle(document.querySelector('#contenu'))"
            ".scrollMarginTop")
        val = float(marge.replace("px", "") or 0)
        v(val >= 60, "ancre @%d : marge de %s" % (w, marge))


# ============================================================= 9. clavier
def s_clavier(pg):
    section("9. clavier et menu")
    pg.set_viewport_size({"width": 390, "height": 780})
    pg.goto(BASE + "fr/index.html", wait_until="networkidle")
    pg.keyboard.press("Tab")
    prem = pg.evaluate("()=>document.activeElement.className")
    v("evitement" in prem, "premier tab : lien d'evitement (%s)" % prem)
    contour = pg.evaluate(
        "()=>{const a=document.querySelector('.evitement');a.focus();"
        "return getComputedStyle(a).outlineWidth;}")
    v(contour not in ("0px", ""), "contour de focus visible (%s)" % contour)
    # le menu s'ouvre et se ferme
    pg.click(".burger")
    v(pg.evaluate("()=>document.getElementById('nav')"
                  ".classList.contains('ouvert')"), "le menu s'ouvre")
    v(pg.get_attribute(".burger", "aria-expanded") == "true",
      "aria-expanded=true a l'ouverture")
    pg.keyboard.press("Escape")
    v(not pg.evaluate("()=>document.getElementById('nav')"
                      ".classList.contains('ouvert')"),
      "Echap ferme le menu")
    # au-dessus du point de bascule le menu est visible : aria-expanded
    # doit dire la verite, sinon on annonce un menu replie qui ne l'est pas
    pg.set_viewport_size({"width": 1280, "height": 800})
    pg.goto(BASE + "fr/index.html", wait_until="networkidle")
    pg.wait_for_timeout(150)
    vis = pg.evaluate(
        "()=>{const e=document.getElementById('nav');"
        "return e?getComputedStyle(e).display:'absent';}")
    v(vis != "none", "menu visible @1280 (%s)" % vis)
    v(pg.get_attribute(".burger", "aria-expanded") == "true",
      "aria-expanded coherent @1280")


# =========================================================== 10. formulaire
def s_formulaire(pg):
    section("10. formulaire")
    pg.set_viewport_size({"width": 1280, "height": 900})
    pg.goto(BASE + "fr/contact.html", wait_until="networkidle")
    # consentement jamais coche d'avance
    v(not pg.is_checked("#k-maquette"), "consentement non coche d'avance")
    v(pg.get_attribute("#c-message", "autocomplete") == "off",
      "champ libre : autocomplete off")
    v(pg.get_attribute("#c-message", "maxlength") == "1200",
      "champ libre borne")
    # soumission vide : erreurs annoncees, aucun message de succes
    pg.click(".formulaire button[type=submit]")
    pg.wait_for_timeout(200)
    v(not pg.is_hidden(".err"), "erreurs annoncees")
    n_err = pg.evaluate("()=>document.querySelectorAll('.err ul li').length")
    v(n_err >= 4, "une entree par champ fautif (%d)" % n_err)
    etat = pg.inner_text(".etat").strip()
    v(etat == "", "aucun message de succes quand le formulaire est invalide")
    # le lien d'erreur DONNE LE FOCUS, il ne fait pas que defiler
    pg.click(".err ul li a")
    pg.wait_for_timeout(120)
    focus = pg.evaluate("()=>document.activeElement.id")
    v(focus == "c-nom", "le lien d'erreur donne le focus (%s)" % focus)
    # soumission valide : message honnete, et AUCUNE adresse de repli
    pg.fill("#c-nom", "Alex")
    pg.fill("#c-contact", "alex")
    pg.select_option("#c-sujet", "forum")
    pg.fill("#c-message", "Bonjour")
    pg.check("#k-maquette")
    pg.click(".formulaire button[type=submit]")
    pg.wait_for_timeout(250)
    etat = pg.inner_text(".etat")
    v("rien n'a" in etat.lower() or "nothing has" in etat.lower(),
      "le message dit que rien n'est parti")
    v(not re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+", etat),
      "aucune adresse inventee dans le message de succes")
    v(not re.search(r"\+\d[\d\s().-]{7,}", etat),
      "aucun numero invente dans le message de succes")
    v(pg.is_hidden(".err"), "la boite d'erreurs disparait")


# ====================================================== 11. sans JavaScript
def s_sans_js(nav):
    section("11. sans JavaScript")
    ctx = nav.new_context(java_script_enabled=False)
    pg = ctx.new_page()

    def attend_css():
        """Attendre que la feuille de style soit APPLIQUEE, pas chargee.

        Avec `domcontentloaded` et une temporisation fixe, la page repond
        avant que la feuille ne soit en vigueur : les elements portent
        alors leurs valeurs par defaut. En local, 120 ms suffisaient ; sur
        la demo en ligne, non — et le controle a rapporte un bouton
        `inline-block` (le defaut d'un <button>) au lieu de `none`,
        c'est-a-dire un defaut du site qui n'existait pas.

        On attend donc une propriete qui ne peut venir QUE de la feuille
        de style : le fond bleu nuit du corps.
        """
        for _ in range(60):
            fond = pg.evaluate(
                "()=>getComputedStyle(document.body).backgroundColor")
            if "7, 11, 20" in fond:
                return True
            pg.wait_for_timeout(100)
        return False

    pg.set_viewport_size({"width": 390, "height": 780})
    pg.goto(BASE + "fr/index.html", wait_until="load")
    v(attend_css(), "sans JS : la feuille de style s'applique")
    # LE POINT CRITIQUE : sans JS, rien ne peut rouvrir un menu replie.
    # Le menu doit donc etre VISIBLE, et le bouton cache.
    vis = pg.evaluate(
        "()=>{const e=document.getElementById('nav');"
        "return e?getComputedStyle(e).display:'absent';}")
    v(vis != "none", "sans JS @390 : le menu reste visible (%s)" % vis)
    bvis = pg.evaluate(
        "()=>getComputedStyle(document.querySelector('.burger')).display")
    v(bvis == "none", "sans JS @390 : le bouton est cache (%s)" % bvis)
    liens = pg.evaluate("()=>document.querySelectorAll('.pied-l a').length")
    v(liens == len(C.PAGES),
      "sans JS : le pied liste les %d pages (%d)" % (len(C.PAGES), liens))
    # le formulaire reste utilisable
    pg.goto(BASE + "fr/contact.html", wait_until="load")
    v(pg.is_visible(".formulaire"), "sans JS : le formulaire est la")
    v(pg.is_hidden(".err"), "sans JS : pas de boite d'erreurs parasite")
    # les etiquettes de statut restent lisibles : c'est du texte
    pg.goto(BASE + "fr/mysteres-de-l-univers.html",
            wait_until="load")
    txt = pg.inner_text("main")
    for mot in ("FAIT", "HYPOTHÈSE"):
        v(mot in txt.upper(),
          "sans JS : l'etiquette « %s » est lisible" % mot)
    ctx.close()


# ======================================================= 12. sans styles
def s_sans_css(nav):
    section("12. sans feuille de style")
    ctx = nav.new_context()
    pg = ctx.new_page()
    pg.route("**/site.css*", lambda r: r.abort())
    pg.goto(BASE + "fr/mysteres-de-l-univers.html",
            wait_until="load")
    pg.wait_for_timeout(150)
    txt = pg.inner_text("body")
    # C'est tout l'interet d'avoir fait des etiquettes du TEXTE : elles
    # survivent a la disparition de la couleur qui les portait.
    for mot in ("Fait", "Hypothèse", "Spéculation"):
        v(mot.upper() in txt.upper(),
          "sans CSS : « %s » reste lisible" % mot)
    ctx.close()


# ========================================================== 13. contrastes
# Le cadrage d'une capture NON pleine page est relatif a la FENETRE, comme
# `getBoundingClientRect` — surtout pas au document. Il faut donc amener
# l'element dans la fenetre, puis relire son rectangle SANS y ajouter le
# defilement.
#
# J'ai fait l'erreur inverse d'abord, en ajoutant `window.scrollY`. Le
# resultat n'a pas ete une erreur franche mais des MESURES FAUSSES : la
# capture photographiait une zone situee un ecran plus bas, et rapportait
# 1,02:1 pour un texte a 8,81:1. Les elements au-dessus de la ligne de
# flottaison, eux, mesuraient juste — les deux lectures coincident quand
# le defilement vaut zero. C'est exactement le genre de panne qui se lit
# comme un defaut du site.
MESURE_JS = """
(sel) => {
  const el = document.querySelector(sel);
  if (!el) return null;
  el.scrollIntoView({block: "center", behavior: "instant"});
  const r = el.getBoundingClientRect();
  return {x: r.x, y: r.y, w: r.width, h: r.height};
}
"""


def contraste_de(pg, sel, nom, resultats):
    """On rend le TEXTE transparent, on photographie, on compare.

    Cacher l'element entier decouvrirait le fond de son ANCETRE, ce qui
    donne une lecture fausse pour tout ce qui peint son propre fond. Et on
    classe les pixels par CONTRASTE, pas par luminance : le fond le plus
    defavorable n'est pas forcement le plus clair ni le plus sombre.
    """
    from PIL import Image
    import io
    boite = pg.evaluate(MESURE_JS, sel)
    if not boite or boite["w"] < 4 or boite["h"] < 4:
        v(False, "contraste : element introuvable (%s)" % nom)
        return
    pg.wait_for_timeout(90)
    couleur = pg.evaluate(
        "(s)=>getComputedStyle(document.querySelector(s)).color", sel)
    m = re.findall(r"[\d.]+", couleur)
    fg = tuple(int(float(x)) for x in m[:3])

    def lum(c):
        def f(u):
            u /= 255.0
            return u / 12.92 if u <= 0.03928 else ((u + 0.055) / 1.055) ** 2.4
        return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])

    def k(a, b):
        la, lb = lum(a), lum(b)
        if la < lb:
            la, lb = lb, la
        return (la + 0.05) / (lb + 0.05)

    # on rentre de 2 px pour ne pas photographier la bordure de l'element
    clip = {"x": boite["x"] + 2, "y": boite["y"] + 2,
            "width": max(4, boite["w"] - 4), "height": max(4, boite["h"] - 4)}

    # TEMOIN. On photographie d'abord le texte VISIBLE, puis le texte
    # transparent, et on exige que les deux images DIFFERENT. Si elles sont
    # identiques, la mesure ne regarde pas le texte : soit le cadrage vise
    # ailleurs, soit la mise en transparence n'a pas pris. Dans les deux
    # cas le chiffre qui suivrait serait invente, et sans ce temoin il
    # ressemblerait a un defaut du site.
    try:
        avant = pg.screenshot(clip=clip)
    except Exception as e:                                    # noqa: BLE001
        v(False, "contraste %s : cadrage impossible (%s)"
          % (nom, str(e)[:60]))
        return

    pg.evaluate("(s)=>{document.querySelector(s).style.color='transparent';}",
                sel)
    try:
        png = pg.screenshot(clip=clip)
    except Exception as e:                                    # noqa: BLE001
        # Un cadrage impossible doit devenir UN echec nomme, pas une pile
        # d'appels : sinon une seule mesure bancale emporte les quinze
        # sections suivantes, et le rapport ne dit plus rien du site.
        pg.evaluate("(s)=>{document.querySelector(s).style.color='';}", sel)
        v(False, "contraste %s : cadrage impossible (%s)"
          % (nom, str(e)[:60]))
        return
    pg.evaluate("(s)=>{document.querySelector(s).style.color='';}", sel)
    if avant == png:
        v(False, "contraste %s : le temoin ne voit pas le texte "
                 "(cadrage ou transparence sans effet)" % nom)
        return
    im = Image.open(io.BytesIO(png)).convert("RGB")
    px = list(im.getdata())
    contrastes = sorted(k(fg, p) for p in px)
    # 2e centile : le fond le plus defavorable, sans se laisser piloter par
    # un pixel isole d'anticrenelage
    pire = contrastes[max(0, int(len(contrastes) * 0.02))]
    resultats.append((nom, pire))
    v(pire >= 4.5, "contraste %s (%.2f:1)" % (nom, pire))


def s_contrastes(pg):
    section("13. contrastes mesures dans le navigateur")
    res = []
    pg.set_viewport_size({"width": 1280, "height": 900})
    pg.goto(BASE + "fr/index.html", wait_until="networkidle")
    for sel, nom in ((".heros h1", "titre du heros"),
                     (".heros .chapo", "chapo du heros"),
                     (".bandeau .dans", "bandeau de demo"),
                     (".convention", "mention de la convention"),
                     (".langue", "bascule de langue"),
                     (".prov", "mention nom de travail"),
                     (".nav a", "lien de menu"),
                     (".carte p", "texte de carte"),
                     (".pied-l a", "lien du pied"),
                     (".pied-p", "note du pied")):
        contraste_de(pg, sel, nom, res)
    pg.goto(BASE + "fr/mysteres-de-l-univers.html", wait_until="networkidle")
    for sel, nom in ((".statut-fait .statut-p", "etiquette Fait"),
                     (".statut-hypothese .statut-p", "etiquette Hypothese"),
                     (".statut-speculation .statut-p",
                      "etiquette Speculation"),
                     (".item p", "texte d'item"),
                     (".encart-avert p", "encart d'avertissement")):
        contraste_de(pg, sel, nom, res)
    pg.goto(BASE + "fr/startups-et-investissement.html",
            wait_until="networkidle")
    contraste_de(pg, ".avert-l li", "avertissement financier", res)
    pg.goto(BASE + "fr/feuille-de-route.html", wait_until="networkidle")
    contraste_de(pg, ".phase-n", "numero de phase", res)
    contraste_de(pg, ".att", "badge d'attente", res)
    contraste_de(pg, ".ind-t", "libelle d'indicateur", res)
    pg.goto(BASE + "fr/contact.html", wait_until="networkidle")
    contraste_de(pg, ".aide", "aide de champ", res)
    contraste_de(pg, ".fil a", "fil d'Ariane", res)
    pg.set_viewport_size({"width": 390, "height": 780})
    pg.goto(BASE + "fr/index.html", wait_until="networkidle")
    contraste_de(pg, ".heros h1", "titre du heros (mobile)", res)
    print("\ncontrastes mesures :")
    for nom, val in res:
        print("   %-34s %6.2f:1" % (nom, val))
    if res:
        print("   %-34s %6.2f:1" % ("--- le plus faible",
                                    min(v for _, v in res)))


# =============================================== 14. mouvement et impression
def s_divers(pg):
    section("14. mouvement reduit et impression")
    ctx = pg.context
    p2 = ctx.new_page()
    p2.emulate_media(reduced_motion="reduce")
    p2.goto(BASE + "fr/index.html", wait_until="networkidle")
    # `getComputedStyle(null)` leve une TypeError et emporte toute la
    # suite. Un element absent doit produire UN echec nomme, pas une pile
    # d'appels : c'est exactement ce qui est arrive quand une mutation a
    # retire les etiquettes de statut, et le banc a lu le plantage comme
    # « -1 echec », c'est-a-dire comme rien du tout.
    d = p2.evaluate(
        "()=>{const e=document.querySelector('.btn');"
        "return e?getComputedStyle(e).transitionDuration:'absent';}")
    # Chromium normalise `0.001ms` en `1e-06s`. La liste des valeurs
    # acceptees decrit ce que le navigateur ECRIT, pas ce que la feuille
    # de style demande.
    v(d in ("0s", "0.001ms", "0.000001s", "1e-06s"),
      "mouvement reduit respecte (%s)" % d)
    p2.emulate_media(media="print")
    p2.wait_for_timeout(100)
    fond = p2.evaluate(
        "()=>getComputedStyle(document.body).backgroundColor")
    v("255, 255, 255" in fond, "impression : fond clair (%s)" % fond)
    # les etiquettes survivent a l'impression : c'est du texte
    p2.goto(BASE + "fr/mysteres-de-l-univers.html", wait_until="networkidle")
    p2.emulate_media(media="print")
    p2.wait_for_timeout(100)
    aff = p2.evaluate(
        "()=>{const e=document.querySelector('.statut');"
        "return e?getComputedStyle(e).display:'absent';}")
    v(aff != "none", "impression : les etiquettes restent (%s)" % aff)
    p2.close()


# ==================================================================== main
def main():
    sources = {}
    for lang, p, rel in toutes_pages():
        sources[rel] = lire(BASE + rel)

    s_structure(sources)
    s_images(sources)
    s_interdits(sources)
    s_attente(sources)
    s_statuts(sources)
    s_liens(sources)

    with sync_playwright() as pw:
        nav = pw.chromium.launch()
        ctx = nav.new_context()
        pg = ctx.new_page()
        s_rendu(pg)
        s_debordement(pg)
        s_ancres(pg)
        s_clavier(pg)
        s_formulaire(pg)
        s_contrastes(pg)
        s_divers(pg)
        ctx.close()
        s_sans_js(nav)
        s_sans_css(nav)
        nav.close()

    print("\n%d controles, %d echecs" % (_ok[0] + len(_ko), len(_ko)))
    for n in _ko:
        print("   ECHEC  " + n)
    return 1 if _ko else 0


if __name__ == "__main__":
    sys.exit(main())
