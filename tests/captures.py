# -*- coding: utf-8 -*-
"""
Apercus du site, dans un navigateur reel.

    python3 tests/captures.py [http://127.0.0.1:8875/]

Aucune capture ne depasse 2000 px dans l'une ou l'autre dimension, et
c'est une assertion, pas une intention : on ne photographie jamais la page
entiere, seulement la fenetre, en la faisant defiler.
"""

import os
import sys

from playwright.sync_api import sync_playwright
from PIL import Image

_ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(_ICI)
SORTIE = os.path.join(RACINE, "apercus")

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8875/"
if not BASE.endswith("/"):
    BASE += "/"

# (nom, page, largeur, hauteur, defilement, action)
VUES = [
    ("01-accueil", "fr/index.html", 1280, 760, 0, None),
    ("02-accueil-branches", "fr/index.html", 1280, 760, 760, None),
    ("03-accueil-etat", "fr/index.html", 1280, 760, 1780, None),
    ("04-forum", "fr/forum.html", 1280, 760, 0, None),
    ("05-forum-regles", "fr/forum.html", 1280, 760, 900, None),
    ("06-mysteres", "fr/mysteres-de-l-univers.html", 1280, 760, 320, None),
    ("07-mysteres-suite", "fr/mysteres-de-l-univers.html", 1280, 760, 1000,
     None),
    ("08-fusees", "fr/fusees-et-lancement.html", 1280, 760, 300, None),
    ("09-robotique", "fr/robotique-spatiale.html", 1280, 760, 300, None),
    ("10-startups-avert", "fr/startups-et-investissement.html", 1280, 760,
     260, None),
    ("11-startups-criteres", "fr/startups-et-investissement.html", 1280, 760,
     820, None),
    ("12-savoirs", "fr/base-de-connaissances.html", 1280, 760, 300, None),
    ("13-ligne-editoriale", "fr/ligne-editoriale.html", 1280, 760, 250, None),
    ("14-ligne-statuts", "fr/ligne-editoriale.html", 1280, 760, 700, None),
    ("15-route", "fr/feuille-de-route.html", 1280, 760, 250, None),
    ("16-route-indicateurs", "fr/feuille-de-route.html", 1280, 760, 1150,
     None),
    ("17-contact", "fr/contact.html", 1280, 760, 250, None),
    ("18-contact-erreurs", "fr/contact.html", 1280, 760, 250, "vide"),
    ("19-contact-valide", "fr/contact.html", 1280, 760, 560, "valide"),
    ("20-mentions", "fr/mentions-legales.html", 1280, 760, 250, None),
    ("21-anglais-accueil", "en/index.html", 1280, 760, 0, None),
    ("22-anglais-mysteres", "en/mysteries-of-the-universe.html", 1280, 760,
     320, None),
    ("23-mobile-accueil", "fr/index.html", 390, 780, 0, None),
    ("24-mobile-menu", "fr/index.html", 390, 780, 0, "menu"),
    ("25-mobile-mysteres", "fr/mysteres-de-l-univers.html", 390, 780, 420,
     None),
    ("26-mobile-startups", "fr/startups-et-investissement.html", 390, 780,
     300, None),
]


def planche_de_marque():
    """La planche est rendue A PARTIR DES SVG DU SITE.

    Redessiner la marque pour la planche laisserait les deux diverger : la
    planche montrerait une version que le site n'utilise pas, et personne
    ne s'en apercevrait avant l'impression.
    """
    a = os.path.join(RACINE, "assets")
    html = """<body style="margin:0;background:#070B14;color:#EDF2F9;
 font:13px/1.5 -apple-system,Segoe UI,Roboto,Arial,sans-serif">
<div style="padding:24px 26px 6px">
 <div style="font:600 19px/1.3 sans-serif;color:#79C0F0">
  Trait plein là où l'on a mesuré. Pointillé là où l'on n'a qu'inféré.</div>
 <div style="color:#A9B6CA;max-width:660px;margin-top:6px">
  Une seule convention : elle est le logo, elle est le motif de fond, elle
  est la façon de dessiner les schémas, et elle est la règle éditoriale.
  Aucune photographie, aucun logo d'agence.</div>
</div>
<div style="display:flex;gap:30px;align-items:flex-end;padding:16px 26px">
 <div><img src="file://%s/marque-duo.svg" width="128">
  <div style="text-align:center;color:#A9B6CA">deux tons</div></div>
 <div><img src="file://%s/marque-accent.svg" width="84">
  <div style="text-align:center;color:#A9B6CA">un ton</div></div>
 <div><img src="file://%s/marque-clair.svg" width="52">
  <div style="text-align:center;color:#A9B6CA">52 px</div></div>
 <div><img src="file://%s/marque-accent.svg" width="34">
  <div style="text-align:center;color:#A9B6CA">34 px</div></div>
 <div style="background:#F4F7FB;padding:14px;border-radius:6px">
  <img src="file://%s/marque-sombre.svg" width="72"></div>
 <div><img src="file://%s/favicon.svg" width="32">
  <div style="text-align:center;color:#A9B6CA">32</div></div>
 <div><img src="file://%s/favicon.svg" width="16">
  <div style="text-align:center;color:#A9B6CA">16</div></div>
</div>
<div style="height:88px;background:#0E1626 url(file://%s/tuile.svg) repeat;
 background-size:180px 180px"></div>
<div style="height:20px;margin:14px 0;
 background:url(file://%s/frise.svg) center/auto 20px repeat-x"></div>
<div style="display:flex;gap:24px;padding:6px 26px 26px;align-items:center">
 <img src="file://%s/schema.svg" width="290">
 <div style="max-width:430px">
  <div style="font:600 15px/1.3 sans-serif;color:#79C0F0">
   Le schéma qui remplace une photographie</div>
  <div style="color:#A9B6CA;margin-top:6px">
   Deux orbites mesurées, et entre elles le transfert en pointillé : il n'a
   pas encore été parcouru.</div>
  <img src="file://%s/legende.svg" width="220" style="margin-top:10px">
  <div style="color:#A9B6CA;margin-top:2px">
   mesuré &nbsp;/&nbsp; inféré</div>
 </div>
</div>
</body>""" % ((a,) * 11)
    chemin = os.path.join(SORTIE, "_planche.html")
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(html)
    return chemin


def main():
    if not os.path.isdir(SORTIE):
        os.makedirs(SORTIE)
    faits = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        ctx = nav.new_context()
        pg = ctx.new_page()

        chemin = planche_de_marque()
        pg.set_viewport_size({"width": 980, "height": 640})
        pg.goto("file://" + chemin)
        pg.wait_for_timeout(350)
        pg.screenshot(path=os.path.join(SORTIE, "do-00-marque.png"))
        faits.append("do-00-marque.png")
        os.remove(chemin)

        for nom, rel, w, h, y, action in VUES:
            pg.set_viewport_size({"width": w, "height": h})
            pg.goto(BASE + rel, wait_until="networkidle")
            pg.wait_for_timeout(220)
            if action == "menu":
                pg.click(".burger")
                pg.wait_for_timeout(180)
            elif action == "vide":
                pg.click(".formulaire button[type=submit]")
                pg.wait_for_timeout(200)
            elif action == "valide":
                pg.fill("#c-nom", "Alex")
                pg.fill("#c-contact", "alex")
                pg.select_option("#c-sujet", "forum")
                pg.fill("#c-message", "Bonjour")
                pg.check("#k-maquette")
                pg.click(".formulaire button[type=submit]")
                pg.wait_for_timeout(250)
            if y:
                pg.evaluate("window.scrollTo(0,%d)" % y)
                pg.wait_for_timeout(220)
            f = os.path.join(SORTIE, "do-%s.png" % nom)
            pg.screenshot(path=f)
            faits.append(os.path.basename(f))
        ctx.close()
        nav.close()

    for n in faits:
        im = Image.open(os.path.join(SORTIE, n))
        assert im.width <= 2000 and im.height <= 2000, \
            "%s : %dx%d" % (n, im.width, im.height)
        print("%-30s %dx%d" % (n, im.width, im.height))
    print("%d apercus" % len(faits))


if __name__ == "__main__":
    main()
