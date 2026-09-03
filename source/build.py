# -*- coding: utf-8 -*-
"""
Construit les 26 pages du site (13 en francais, 13 en anglais), la page
d'aiguillage, le plan de site et le robots.txt.

    python3 source/build.py

Les fichiers .html ne se modifient JAMAIS a la main : ils sont ecrases au
prochain passage. Toute correction se fait ici ou dans contenu.py.

DEMO = True pose trois choses ENSEMBLE, et il faut les trois : le bandeau
de demonstration, la balise `noindex` sur chaque page, et un robots.txt
ferme. Un robots.txt seul n'empeche pas l'indexation d'une URL deja connue.
"""

import html
import os
import sys

_ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(_ICI) if os.path.basename(_ICI) == "source" else _ICI
sys.path.insert(0, _ICI)

import contenu as C  # noqa: E402
import motif as M  # noqa: E402

DEMO = True
VERSION_CSS = 1
BASE = "https://anirudhatalmale6-alt.github.io/deep-orbit-network/"

LANGS = ("fr", "en")
IDX = {"fr": 0, "en": 1}


def t(couple, lang):
    """Un couple (fr, en) -> la bonne moitie. Echappee, toujours."""
    return html.escape(couple[IDX[lang]])


def tb(couple, lang):
    """Idem, mais sans echappement : reserve aux chaines qui contiennent
    deja du balisage produit ici, jamais a du texte venant d'ailleurs."""
    return couple[IDX[lang]]


def fichier(page, lang):
    return page[IDX[lang]]


def titre(page, lang):
    return page[2 + IDX[lang]]


def menu(page, lang):
    return page[4 + IDX[lang]]


def autre_lang(lang):
    return "en" if lang == "fr" else "fr"


# --------------------------------------------------------------- fragments
def badge_statut(cle, lang):
    """L'etiquette de statut.

    C'est du TEXTE, pas une couleur : elle se lit a voix haute, elle
    survit a l'impression et elle existe encore quand la feuille de style
    ne se charge pas. Le `title` porte la definition complete, et cette
    definition est aussi ecrite en clair sur la page ligne editoriale —
    un `title` seul n'est pas accessible au clavier ni au toucher.
    """
    nom, definition = C.STATUTS[cle]
    return ('<span class="statut statut-%s"><span class="statut-p">%s</span>'
            '<span class="sr">, %s</span></span>'
            % (cle, t(nom, lang), t(definition, lang)))


def bloc_attentes(items, lang, titre_couple=None):
    """Les blocs « ce qui reste a valider ».

    Chacun porte le mot d'attente de ce chantier et la CONDITION exacte qui
    le levera. Un manque sans sa condition ressemble a un oubli ; avec sa
    condition, c'est une decision qui attend quelqu'un.
    """
    o = []
    if titre_couple is not None:
        o.append('<h2>%s</h2>' % t(titre_couple, lang))
    o.append('<ul class="attentes">')
    for it in items:
        o.append('<li class="attente">')
        o.append('<p class="att">%s</p>' % t(C.ATTENTE, lang))
        o.append('<h3>%s</h3>' % t((it[0], it[1]), lang))
        o.append('<p>%s</p>' % t((it[2], it[3]), lang))
        o.append('</li>')
    o.append('</ul>')
    return "\n".join(o)


def cartes(items, lang, lien=False, prefixe=""):
    o = ['<ul class="g3">']
    for it in items:
        o.append('<li class="carte">')
        if lien and len(it) > 4:
            cible = it[4] if lang == "fr" else _en(it[4])
            o.append('<h3><a href="%s%s">%s</a></h3>'
                     % (prefixe, cible, t((it[0], it[1]), lang)))
        else:
            o.append('<h3>%s</h3>' % t((it[0], it[1]), lang))
        o.append('<p>%s</p>' % t((it[2], it[3]), lang))
        o.append('</li>')
    o.append('</ul>')
    return "\n".join(o)


_PAR_FR = {}
for _p in C.PAGES:
    _PAR_FR[_p[0]] = _p[1]


def _en(fichier_fr):
    return _PAR_FR[fichier_fr]


def liste_simple(items, lang, classe="liste"):
    o = ['<ul class="%s">' % classe]
    for it in items:
        o.append('<li>%s</li>' % t(it, lang))
    o.append('</ul>')
    return "\n".join(o)


def paragraphes(items, lang):
    return "\n".join('<p>%s</p>' % t(it, lang) for it in items)


# ------------------------------------------------------------------ gabarit
def entete(page, lang):
    o = []
    o.append('<a class="evitement" href="#contenu">%s</a>'
             % t(C.EVITEMENT, lang))
    if DEMO:
        o.append('<div class="bandeau" role="note"><div class="dans">%s</div>'
                 '</div>' % t(C.DEMO_BANDEAU, lang))
    o.append('<div class="util"><div class="dans">')
    o.append('<p class="convention">%s</p>' % t(C.CONVENTION, lang))
    o.append('<a class="langue" href="../%s/%s" hreflang="%s" lang="%s">%s</a>'
             % (autre_lang(lang), fichier(page, autre_lang(lang)),
                autre_lang(lang), autre_lang(lang),
                t(C.LANGUE_AUTRE, lang)))
    o.append('</div></div>')
    o.append('<header class="entete"><div class="dans">')
    o.append('<a class="marque" href="index.html">')
    o.append('<img src="../assets/marque-duo.svg" alt="" width="42" '
             'height="42">')
    o.append('<span class="marque-t"><span class="marque-n">%s</span>'
             '<span class="prov">%s</span></span>'
             % (t(C.MARQUE, lang), t(C.NOM_TRAVAIL, lang)))
    o.append('</a>')
    o.append('<button class="burger" type="button" aria-expanded="false" '
             'aria-controls="nav">%s</button>' % t(C.MENU, lang))
    o.append('<nav id="nav" class="nav" aria-label="%s">' % t(C.MENU, lang))
    o.append('<ul>')
    for p in C.PAGES:
        if menu(p, lang) is None:
            continue
        actif = ' aria-current="page"' if p is page else ''
        o.append('<li><a href="%s"%s>%s</a></li>'
                 % (fichier(p, lang), actif, html.escape(menu(p, lang))))
    o.append('</ul></nav>')
    o.append('</div></header>')
    return "\n".join(o)


def fil(page, lang):
    if page is C.PAGES[0]:
        return ""
    return ('<nav class="fil" aria-label="%s"><div class="dans">'
            '<a href="index.html">%s</a> <span aria-hidden="true">/</span> '
            '<span>%s</span></div></nav>'
            % (t(C.FIL, lang), html.escape(menu(C.PAGES[0], lang)),
               html.escape(titre(page, lang))))


def pied(lang):
    o = ['<footer class="pied"><div class="dans">']
    o.append('<div class="pied-g">')
    o.append('<div>')
    o.append('<img src="../assets/marque-clair.svg" alt="" width="36" '
             'height="36">')
    o.append('<p class="pied-n">%s <span class="prov">%s</span></p>'
             % (t(C.MARQUE, lang), t(C.NOM_TRAVAIL, lang)))
    o.append('<p class="pied-p">%s</p>' % t(C.NOM_TRAVAIL_LONG, lang))
    o.append('</div>')
    o.append('<nav aria-label="%s"><ul class="pied-l">' % t(C.MENU, lang))
    for p in C.PAGES:
        o.append('<li><a href="%s">%s</a></li>'
                 % (fichier(p, lang), html.escape(titre(p, lang))))
    o.append('</ul></nav>')
    o.append('</div>')
    o.append('<p class="pied-p">%s</p>' % t(C.PIED_NOTE, lang))
    o.append('</div></footer>')
    return "\n".join(o)


def page_html(page, lang, corps):
    fr_f = fichier(page, "fr")
    en_f = fichier(page, "en")
    o = ['<!doctype html>', '<html lang="%s">' % lang, '<head>',
         '<meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,'
         'initial-scale=1">',
         '<title>%s — %s</title>' % (html.escape(titre(page, lang)),
                                     t(C.MARQUE, lang)),
         '<meta name="description" content="%s">'
         % t(C.META[fr_f], lang)]
    if DEMO:
        o.append('<meta name="robots" content="noindex,nofollow">')
    o.append('<link rel="canonical" href="%s%s/%s">' % (BASE, lang,
                                                        fichier(page, lang)))
    o.append('<link rel="alternate" hreflang="fr" href="%sfr/%s">'
             % (BASE, fr_f))
    o.append('<link rel="alternate" hreflang="en" href="%sen/%s">'
             % (BASE, en_f))
    o.append('<link rel="alternate" hreflang="x-default" href="%sen/%s">'
             % (BASE, en_f))
    o.append('<link rel="icon" href="../assets/favicon.svg" '
             'type="image/svg+xml">')
    o.append('<link rel="stylesheet" href="../assets/site.css?v=%d">'
             % VERSION_CSS)
    # Pas de donnees structurees. Declarer une Organization dont le nom est
    # un nom de travail, sans pays, sans adresse et sans forme juridique,
    # publie une identite qui n'existe pas ; et c'est exactement ce qu'un
    # moteur recopierait dans un panneau de resultats. Le probleme est pire
    # ici que sur un site ordinaire : le cahier des charges parle d'un fonds
    # d'investissement, et une fiche « Organization » aupres d'un moteur est
    # precisement ce qui ferait croire qu'il existe.
    o.append('</head><body>')
    o.append(entete(page, lang))
    o.append(fil(page, lang))
    o.append('<main id="contenu" tabindex="-1">')
    o.append(corps)
    o.append('</main>')
    o.append(pied(lang))
    o.append('<script src="../assets/site.js?v=%d" defer></script>'
             % VERSION_CSS)
    o.append('</body></html>')
    return "\n".join(o)


# -------------------------------------------------------------------- corps
def heros(titre_c, chapo_c, lang, marque=True):
    o = ['<section class="heros"><div class="dans"><div class="heros-g">']
    o.append('<div>')
    if marque:
        o.append('<img class="heros-m" src="../assets/marque-accent.svg" '
                 'alt="" width="72" height="72">')
    o.append('<h1>%s</h1>' % t(titre_c, lang))
    o.append('<p class="chapo">%s</p>' % t(chapo_c, lang))
    o.append('</div>')
    o.append('<div class="heros-i"><img src="../assets/schema.svg" alt="" '
             'width="420" height="300"></div>')
    o.append('</div></div></section>')
    return "\n".join(o)


def titre_page(page, lang, chapo_c):
    return ('<section class="titre"><div class="dans">'
            '<h1>%s</h1><p class="chapo">%s</p></div></section>'
            % (html.escape(titre(page, lang)), t(chapo_c, lang)))


def encart(texte_c, lang, ton="note"):
    return ('<div class="encart encart-%s"><div class="dans"><p>%s</p>'
            '</div></div>' % (ton, t(texte_c, lang)))


def corps_accueil(page, lang):
    o = [heros(C.ACC_TITRE, C.ACC_CHAPO, lang)]
    o.append('<section class="dans"><p class="intro">%s</p></section>'
             % t(C.ACC_INTRO, lang))
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % ("Les six branches" if lang == "fr" else "The six branches",
                cartes(C.ACC_BRANCHES, lang, lien=True)))
    o.append('<div class="frise" aria-hidden="true"></div>')
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % (t(C.ACC_PUBLICS_TITRE, lang),
                cartes(C.ACC_PUBLICS, lang)))
    o.append('<section class="dans etat"><h2>%s</h2>%s</section>'
             % (t(C.ACC_ETAT_TITRE, lang), paragraphes(C.ACC_ETAT, lang)))
    o.append('<section class="dans"><p><a class="btn" href="%s">%s</a></p>'
             '</section>'
             % (fichier(C.PAGES[7], lang), t(C.ALLER_PLUS, lang)))
    return "\n".join(o)


def corps_forum(page, lang):
    o = [titre_page(page, lang, C.FORUM_CHAPO)]
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % ("Les dix catégories" if lang == "fr" else "The ten categories",
                liste_simple(C.FORUM_CATEGORIES, lang, "categories")))
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % (t(C.FORUM_REGLES_TITRE, lang),
                liste_simple(C.FORUM_REGLES, lang, "regles")))
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % (t(C.FORUM_MODERATION_TITRE, lang),
                liste_simple(C.FORUM_MODERATION, lang, "regles")))
    o.append('<section class="dans">%s</section>'
             % bloc_attentes(C.FORUM_ATTENTES, lang, C.ATTENTE_TITRE))
    return "\n".join(o)


def corps_mysteres(page, lang):
    o = [titre_page(page, lang, C.MYST_CHAPO)]
    o.append(encart(C.MYST_AVERT, lang, "avert"))
    o.append('<section class="dans">')
    for sujet in C.MYST_SUJETS:
        o.append('<article class="sujet">')
        o.append('<h2>%s</h2>' % t((sujet[0], sujet[1]), lang))
        for cle, fr, en in sujet[2]:
            o.append('<div class="item">')
            o.append(badge_statut(cle, lang))
            o.append('<p>%s</p>' % t((fr, en), lang))
            o.append('</div>')
        o.append('</article>')
    o.append('</section>')
    o.append('<section class="dans">%s</section>'
             % bloc_attentes(C.MYST_ATTENTES, lang, C.ATTENTE_TITRE))
    return "\n".join(o)


def corps_fusees(page, lang):
    o = [titre_page(page, lang, C.FUS_CHAPO)]
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % (t(C.FUS_TITRE, lang), cartes(C.FUS_SUJETS, lang)))
    o.append('<section class="dans">%s</section>'
             % bloc_attentes(C.FUS_ATTENTES, lang, C.ATTENTE_TITRE))
    return "\n".join(o)


def corps_robotique(page, lang):
    o = [titre_page(page, lang, C.ROB_CHAPO)]
    o.append(encart(C.ROB_AVERT, lang, "avert"))
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % (t(C.ROB_TITRE, lang), cartes(C.ROB_AXES, lang)))
    o.append('<section class="dans">%s</section>'
             % bloc_attentes(C.ROB_ATTENTES, lang, C.ATTENTE_TITRE))
    return "\n".join(o)


def corps_startups(page, lang):
    o = [titre_page(page, lang, C.INV_CHAPO)]
    # L'avertissement est EN TETE, pas en bas de page. Un avertissement
    # place apres le contenu qu'il corrige n'est pas lu par ceux qu'il
    # devrait protéger.
    o.append('<section class="dans avert-bloc">')
    o.append('<h2>%s</h2>' % t(C.INV_AVERT_TITRE, lang))
    o.append('<ul class="avert-l">')
    for it in C.INV_AVERT:
        o.append('<li>%s</li>' % t(it, lang))
    o.append('</ul></section>')
    o.append('<section class="dans"><h2>%s</h2><p class="note">%s</p>%s'
             '</section>'
             % (t(C.INV_CRITERES_TITRE, lang), t(C.INV_CRITERES_NOTE, lang),
                cartes(C.INV_CRITERES, lang)))
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % (t(C.INV_SECTEURS_TITRE, lang),
                liste_simple(C.INV_SECTEURS, lang, "categories")))
    o.append('<section class="dans">%s</section>'
             % bloc_attentes(C.INV_ATTENTES, lang, C.ATTENTE_TITRE))
    return "\n".join(o)


def corps_savoirs(page, lang):
    o = [titre_page(page, lang, C.SAV_CHAPO)]
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % (t(C.SAV_TITRE, lang), cartes(C.SAV_TYPES, lang)))
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % (t(C.SAV_STRUCTURE_TITRE, lang),
                cartes(C.SAV_STRUCTURE, lang)))
    o.append('<section class="dans">%s</section>'
             % bloc_attentes(C.SAV_ATTENTES, lang, C.ATTENTE_TITRE))
    return "\n".join(o)


def corps_ligne(page, lang):
    o = [titre_page(page, lang, C.LED_CHAPO)]
    o.append('<section class="dans convention-bloc">')
    o.append('<img src="../assets/legende.svg" alt="" width="300" '
             'height="74">')
    o.append('<div><p class="conv-t">%s</p><p>%s</p></div>'
             % (t(C.CONVENTION, lang), t(C.CONVENTION_TEXTE, lang)))
    o.append('</section>')
    o.append('<section class="dans"><h2>%s</h2><ul class="statuts">'
             % ("Les quatre statuts" if lang == "fr"
                else "The four statuses"))
    for cle in ("fait", "hypothese", "opinion", "speculation"):
        nom, definition = C.STATUTS[cle]
        o.append('<li><span class="statut statut-%s">'
                 '<span class="statut-p">%s</span></span>'
                 '<p>%s</p></li>' % (cle, t(nom, lang), t(definition, lang)))
    o.append('</ul></section>')
    o.append('<section class="dans"><h2>%s</h2><p>%s</p></section>'
             % ("Pourquoi l'étiquette est du texte" if lang == "fr"
                else "Why the label is text", t(C.LED_POURQUOI, lang)))
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % (t(C.LED_REGLES_TITRE, lang),
                liste_simple(C.LED_REGLES, lang, "regles")))
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % (t(C.LED_REVUE_TITRE, lang),
                liste_simple(C.LED_REVUE, lang, "regles")))
    o.append('<section class="dans">%s</section>'
             % bloc_attentes(C.LED_ATTENTES, lang, C.ATTENTE_TITRE))
    return "\n".join(o)


def corps_route(page, lang):
    o = [titre_page(page, lang, C.FDR_CHAPO)]
    o.append('<section class="dans"><ol class="phases">')
    for n, tfr, ten, lfr, len_, etat in C.FDR_PHASES:
        o.append('<li class="phase">')
        o.append('<p class="phase-n">%s</p>' % html.escape(n))
        o.append('<h2>%s</h2>' % t((tfr, ten), lang))
        o.append('<p>%s</p>' % t((lfr, len_), lang))
        o.append('<p class="phase-e">%s</p>' % t(etat, lang))
        o.append('</li>')
    o.append('</ol>')
    o.append('<p class="note">%s</p>' % t(C.FDR_PHASE1_NOTE, lang))
    o.append('</section>')
    o.append('<section class="dans"><h2>%s</h2><p class="note">%s</p>%s'
             '</section>'
             % (t(C.FDR_IND_TITRE, lang), t(C.FDR_IND_NOTE, lang),
                indicateurs(C.FDR_INDICATEURS, lang)))
    return "\n".join(o)


def indicateurs(items, lang):
    """Les indicateurs, affiches SANS valeur.

    La colonne de droite porte le mot d'attente, pas un tiret ni un zero :
    un zero est une mesure, et personne n'a mesure.
    """
    o = ['<ul class="indicateurs">']
    for it in items:
        o.append('<li><span class="ind-t">%s</span>'
                 '<span class="att att-i">%s</span></li>'
                 % (t(it, lang), t(C.ATTENTE, lang)))
    o.append('</ul>')
    return "\n".join(o)


def corps_contact(page, lang):
    o = [titre_page(page, lang, C.CON_CHAPO)]
    o.append('<section class="dans"><form class="formulaire" novalidate>')
    o.append('<div class="err" role="alert" hidden><p class="err-t">%s</p>'
             '<ul></ul></div>' % t(C.CON_ERREUR_RESUME, lang))
    for cle in ("nom", "contact", "sujet", "message"):
        etiq, aide = C.CON_CHAMPS[cle]
        o.append('<p class="champ">')
        o.append('<label for="c-%s">%s</label>' % (cle, t(etiq, lang)))
        if aide[0]:
            o.append('<span class="aide" id="a-%s">%s</span>'
                     % (cle, t(aide, lang)))
        decrit = ' aria-describedby="a-%s"' % cle if aide[0] else ''
        if cle == "sujet":
            o.append('<select id="c-sujet" name="sujet" required%s>' % decrit)
            for val, lib in C.CON_SUJETS:
                o.append('<option value="%s">%s</option>'
                         % (html.escape(val), t(lib, lang)))
            o.append('</select>')
        elif cle == "message":
            o.append('<textarea id="c-message" name="message" rows="5" '
                     'maxlength="1200" autocomplete="off" required%s>'
                     '</textarea>' % decrit)
        else:
            o.append('<input id="c-%s" name="%s" type="text" maxlength="120" '
                     'required%s>' % (cle, cle, decrit))
        o.append('</p>')
    o.append('<p class="champ-c"><label><input type="checkbox" '
             'id="k-maquette" name="maquette" required> <span>%s</span>'
             '</label></p>' % t(C.CON_CONSENTEMENT, lang))
    o.append('<p><button class="btn" type="submit">%s</button></p>'
             % ("Envoyer" if lang == "fr" else "Send"))
    o.append('<p class="etat" role="status"></p>')
    o.append('</form></section>')
    o.append('<section class="dans">%s</section>'
             % bloc_attentes(C.CON_ATTENTES, lang, C.ATTENTE_TITRE))
    return "\n".join(o)


def corps_mentions(page, lang):
    o = [titre_page(page, lang, C.MENT_CHAPO)]
    o.append('<section class="dans">%s</section>'
             % bloc_attentes(C.MENT_ATTENTES, lang, C.ATTENTE_TITRE))
    return "\n".join(o)


def corps_confidentialite(page, lang):
    o = [titre_page(page, lang, C.CONF_CHAPO)]
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % ("Ce qui est vrai aujourd'hui" if lang == "fr"
                else "What is true today",
                liste_simple(C.CONF_FAITS, lang, "regles")))
    o.append('<section class="dans">%s</section>'
             % bloc_attentes(C.CONF_ATTENTES, lang, C.ATTENTE_TITRE))
    return "\n".join(o)


def corps_accessibilite(page, lang):
    o = [titre_page(page, lang, C.ACCESS_CHAPO)]
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % ("Ce qui a été fait" if lang == "fr" else "What has been done",
                liste_simple(C.ACCESS_FAIT, lang, "regles")))
    o.append('<section class="dans"><h2>%s</h2>%s</section>'
             % ("Ce qui n'a pas été fait" if lang == "fr"
                else "What has not been done",
                liste_simple(C.ACCESS_PAS_FAIT, lang, "regles")))
    return "\n".join(o)


CORPS = {
    "index.html": corps_accueil,
    "forum.html": corps_forum,
    "mysteres-de-l-univers.html": corps_mysteres,
    "fusees-et-lancement.html": corps_fusees,
    "robotique-spatiale.html": corps_robotique,
    "startups-et-investissement.html": corps_startups,
    "base-de-connaissances.html": corps_savoirs,
    "ligne-editoriale.html": corps_ligne,
    "feuille-de-route.html": corps_route,
    "contact.html": corps_contact,
    "mentions-legales.html": corps_mentions,
    "confidentialite.html": corps_confidentialite,
    "accessibilite.html": corps_accessibilite,
}


# ------------------------------------------------------------------ racine
def aiguillage():
    """Page racine : elle ne choisit PAS la langue a la place du lecteur.

    Une redirection automatique sur `navigator.language` envoie un
    francophone sur la version anglaise des qu'il emprunte un navigateur,
    et rend la page inatteignable pour l'autre moitie. Deux liens, egaux.
    """
    o = ['<!doctype html>', '<html lang="en">', '<head>',
         '<meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,'
         'initial-scale=1">',
         '<title>%s</title>' % html.escape(C.MARQUE[1])]
    if DEMO:
        o.append('<meta name="robots" content="noindex,nofollow">')
    o.append('<link rel="icon" href="assets/favicon.svg" '
             'type="image/svg+xml">')
    o.append('<link rel="alternate" hreflang="fr" href="%sfr/index.html">'
             % BASE)
    o.append('<link rel="alternate" hreflang="en" href="%sen/index.html">'
             % BASE)
    o.append('<link rel="stylesheet" href="assets/site.css?v=%d">'
             % VERSION_CSS)
    o.append('</head><body class="aiguillage">')
    o.append('<main id="contenu"><div class="dans">')
    o.append('<img src="assets/marque-duo.svg" alt="" width="86" '
             'height="86">')
    o.append('<h1>%s <span class="prov">%s</span></h1>'
             % (html.escape(C.MARQUE[1]), html.escape(C.NOM_TRAVAIL[1])))
    o.append('<p>%s</p>' % html.escape(C.BASELINE[1]))
    o.append('<p class="aig-l"><a class="btn" href="fr/index.html" '
             'hreflang="fr" lang="fr">Français</a> '
             '<a class="btn" href="en/index.html" hreflang="en" '
             'lang="en">English</a></p>')
    o.append('<p class="note">%s</p>' % html.escape(C.DEMO_BANDEAU[1]))
    o.append('</div></main></body></html>')
    return "\n".join(o)


def sitemap():
    o = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
         'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for p in C.PAGES:
        for lang in LANGS:
            o.append('<url><loc>%s%s/%s</loc>' % (BASE, lang,
                                                  fichier(p, lang)))
            for autre in LANGS:
                o.append('<xhtml:link rel="alternate" hreflang="%s" '
                         'href="%s%s/%s"/>'
                         % (autre, BASE, autre, fichier(p, autre)))
            o.append('</url>')
    o.append('</urlset>')
    return "\n".join(o)


def robots():
    if DEMO:
        return "User-agent: *\nDisallow: /\n"
    return "User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n" % BASE


def main():
    M.ecrire()
    n = 0
    for lang in LANGS:
        d = os.path.join(RACINE, lang)
        if not os.path.isdir(d):
            os.makedirs(d)
        for p in C.PAGES:
            corps = CORPS[p[0]](p, lang)
            with open(os.path.join(d, fichier(p, lang)), "w",
                      encoding="utf-8") as f:
                f.write(page_html(p, lang, corps) + "\n")
            n += 1
    for nom, contenu in (("index.html", aiguillage()),
                         ("sitemap.xml", sitemap()),
                         ("robots.txt", robots())):
        with open(os.path.join(RACINE, nom), "w", encoding="utf-8") as f:
            f.write(contenu + ("\n" if not contenu.endswith("\n") else ""))
    print("%d pages + aiguillage + sitemap + robots" % n)
    return n


if __name__ == "__main__":
    main()
