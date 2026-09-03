# -*- coding: utf-8 -*-
"""
Ornements de la plateforme spatiale.

Tout sort d'une seule idee, et cette idee est le chapitre 11 du cahier des
charges : distinguer le fait de l'hypothese.

    UN TRAIT PLEIN LA OU L'ON A MESURE.
    UN TRAIT POINTILLE LA OU L'ON N'A QU'INFERE.

C'est la marque, c'est le motif de fond, c'est la maniere dont les schemas
sont dessines, et c'est aussi la regle editoriale du site. Le lecteur
apprend la convention sur le logo et la retrouve partout ailleurs.

Deux consequences volontaires :

* AUCUNE photographie. Ni de mission, ni de fusee, ni de planete, ni
  d'ingenieur. Une photo de lancement trouvee quelque part est presque
  toujours la propriete d'une agence ou d'un industriel, et une image de
  nebuleuse « generique » publiee sous un titre precis affirme un fait que
  personne n'a verifie. Les emplacements d'image portent un schema dessine.

* AUCUN logo d'agence, de lanceur ou d'entreprise reelle. Le chapitre 11
  interdit les fausses affirmations ; afficher l'embleme d'une agence sur un
  site qui n'a aucun lien avec elle en est une, et c'est en plus une
  usurpation.

Les noms de fichiers sont neutres — accent, clair, sombre, duo — et pas des
noms de couleur : sur le chantier precedent la palette a change en cours de
route, et des fichiers nommes d'apres une teinte auraient force a renommer
partout.
"""

import math
import os

_ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(_ICI) if os.path.basename(_ICI) == "source" else _ICI
ACTIFS = os.path.join(RACINE, "assets")

# ---------------------------------------------------------------- palette
# Chapitre 12 : « fonds bleu nuit ou noir, lignes orbitales, schemas
# techniques, typographie propre ». La palette est donc sombre par defaut.
#
# Chaque valeur de TEXTE est calculee avant d'etre ecrite, puis remesuree
# dans un navigateur reel (voir README, « Contrastes mesures »).
# ACCENT et AMBRE ne servent JAMAIS de texte sur fond clair : ils sont
# calibres pour le fond sombre. Sur fond clair ce sont ACCENT_SOMBRE et
# AMBRE_SOMBRE qui prennent le relais.
NUIT = "#070B14"        # fond general
PANNEAU = "#0E1626"     # cartes et panneaux
ARDOISE = "#1B2739"     # bordures et separateurs
CLAIR = "#EDF2F9"       # texte principal sur fond sombre
DOUX = "#A9B6CA"        # texte secondaire sur fond sombre
ACCENT = "#79C0F0"      # le trait PLEIN : ce qui est mesure
AMBRE = "#E9B168"       # le trait POINTILLE : ce qui est infere
BLANC = "#FFFFFF"
PAPIER = "#F4F7FB"      # fond clair (impression, sections claires)
ENCRE = "#101927"       # texte sur fond clair
ENCRE_DOUX = "#42506A"  # texte secondaire sur fond clair
ACCENT_SOMBRE = "#1D5C8A"   # l'accent, version texte sur fond clair
AMBRE_SOMBRE = "#7A4E12"    # l'ambre, version texte sur fond clair

# ---------------------------------------------------------------- geometrie
LARGEUR = 200.0
HAUTEUR = 200.0
CX = LARGEUR / 2.0
CY = HAUTEUR / 2.0

R_ORBITE = 74.0
EP_ORBITE = 9.0
# L'arc plein couvre la portion OBSERVEE, le pointille la portion INFEREE.
# 232 degres pleins : assez pour que la figure se lise comme une orbite,
# assez peu pour que le pointille reste une part visible et non un detail.
DEBUT_PLEIN = 128.0
ETENDUE_PLEIN = 232.0

R_CORPS = 15.0


def _f(v):
    """3 decimales max, sans zeros inutiles : les SVG restent lisibles."""
    s = "%.3f" % v
    s = s.rstrip("0").rstrip(".")
    return s if s not in ("", "-0") else "0"


def _pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def arc(cx, cy, r, debut, etendue):
    """Arc decrit par son DEBUT et son ETENDUE, en degres.

    On decrit l'etendue plutot que le point d'arrivee parce que c'est elle
    qui porte le sens ici : elle dit quelle PART de l'orbite a ete observee.
    La regler, c'est regler le rapport entre le mesure et l'infere, et c'est
    le seul reglage de cette marque qui change ce qu'elle raconte.
    """
    x0, y0 = _pt(cx, cy, r, debut)
    x1, y1 = _pt(cx, cy, r, debut + etendue)
    grand = 1 if abs(etendue) % 360.0 > 180.0 else 0
    sens = 1 if etendue > 0 else 0
    return "M %s %s A %s %s 0 %d %d %s %s" % (_f(x0), _f(y0), _f(r), _f(r),
                                              grand, sens, _f(x1), _f(y1))


def _entete(largeur, hauteur, titre):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" '
            'width="%s" height="%s" role="img" aria-label="%s">'
            % (_f(largeur), _f(hauteur), _f(largeur), _f(hauteur), titre))


def marque(mesure=ACCENT, infere=AMBRE, corps=None,
           titre="Orbite mesuree et orbite inferee"):
    """La marque : une orbite pleine la ou l'on a mesure, pointillee ailleurs.

    Le pointille n'est pas un ornement. Il occupe la portion de l'orbite
    que personne n'a observee, et il est de la meme epaisseur que le plein
    pour qu'on lise « meme trajectoire, statut different » et non
    « trait principal et trait secondaire ».

    Le corps central est plein : c'est la seule chose dont l'existence
    n'est pas en discussion.
    """
    c = corps or mesure
    reste = 360.0 - ETENDUE_PLEIN
    o = [_entete(LARGEUR, HAUTEUR, titre)]
    o.append('<g fill="none" stroke-linecap="round">')
    o.append('<path d="%s" stroke="%s" stroke-width="%s"/>'
             % (arc(CX, CY, R_ORBITE, DEBUT_PLEIN, ETENDUE_PLEIN), mesure,
                _f(EP_ORBITE)))
    o.append('<path d="%s" stroke="%s" stroke-width="%s" '
             'stroke-dasharray="2 17"/>'
             % (arc(CX, CY, R_ORBITE, DEBUT_PLEIN + ETENDUE_PLEIN, reste),
                infere, _f(EP_ORBITE)))
    o.append("</g>")
    o.append('<circle cx="%s" cy="%s" r="%s" fill="%s"/>'
             % (_f(CX), _f(CY), _f(R_CORPS), c))
    o.append("</svg>")
    return "\n".join(o)


def favicon(fond=PANNEAU, mesure=ACCENT, infere=AMBRE):
    """32 px : le pointille fin disparaitrait, il est donc regle plus large.

    A cette taille un `stroke-dasharray` de 2 sur 17 se lit comme une ligne
    sale ou comme rien du tout. Les tirets sont donc proportionnellement
    plus gros et moins nombreux : trois interruptions franches valent mieux
    que douze invisibles.
    """
    o = [_entete(64, 64, "Orbite mesuree et orbite inferee")]
    o.append('<rect width="64" height="64" rx="13" fill="%s"/>' % fond)
    o.append('<g fill="none" stroke-linecap="round" stroke-width="6">')
    o.append('<path d="%s" stroke="%s"/>'
             % (arc(32, 32, 20, 128.0, 232.0), mesure))
    o.append('<path d="%s" stroke="%s" stroke-dasharray="3 9"/>'
             % (arc(32, 32, 20, 0.0, 128.0), infere))
    o.append("</g>")
    o.append('<circle cx="32" cy="32" r="5" fill="%s"/>' % mesure)
    o.append("</svg>")
    return "\n".join(o)


def tuile(cote=180.0, mesure=ACCENT, infere=AMBRE, epaisseur=1.1):
    """Fond repete : des arcs orbitaux, tres faiblement opaques.

    Les quatre coins portent le MEME arc, sinon le motif ne se raccorde pas
    quand `background-repeat` le repete : chaque coin ne montre qu'un quart
    de cercle et c'est le quart du voisin qui le complete.

    Le rayon vaut 0,38 fois le cote et non la moitie : a la moitie exacte,
    les cercles voisins se coupent au milieu de chaque bord et dessinent une
    file d'ogives pointues, un motif d'architecture qui n'a rien a faire sur
    un fond de ciel.
    """
    r = cote * 0.38
    o = [_entete(cote, cote, "Motif orbital")]
    o.append('<g fill="none" stroke-linecap="round" stroke-width="%s">'
             % _f(epaisseur))
    for cx, cy in ((0, 0), (cote, 0), (0, cote), (cote, cote)):
        o.append('<path d="%s" stroke="%s"/>' % (arc(cx, cy, r, 0.0, 90.0),
                                                 mesure))
    o.append('<path d="%s" stroke="%s" stroke-dasharray="2 8"/>'
             % (arc(cote * 0.5, cote * 0.5, cote * 0.22, 150.0, 250.0),
                infere))
    o.append("</g>")
    o.append('<circle cx="%s" cy="%s" r="2.2" fill="%s"/>'
             % (_f(cote * 0.5), _f(cote * 0.5), mesure))
    o.append("</svg>")
    return "\n".join(o)


def frise(largeur=1200.0, hauteur=20.0, mesure=ACCENT, infere=AMBRE,
          pas=150.0):
    """Separateur : un trait qui alterne mesure et inference.

    Purement decoratif — d'ou `aria-hidden` partout ou il est pose, et d'ou
    le fait que son contraste ne pose pas de probleme : il ne porte aucune
    information.
    """
    cy = hauteur / 2.0
    o = [_entete(largeur, hauteur, "Frise")]
    x = 0.0
    while x < largeur:
        fin = min(x + pas * 0.62, largeur)
        o.append('<path d="M %s %s L %s %s" stroke="%s" stroke-width="1.1" '
                 'stroke-linecap="round"/>'
                 % (_f(x), _f(cy), _f(fin), _f(cy), mesure))
        if fin < largeur:
            o.append('<path d="M %s %s L %s %s" stroke="%s" '
                     'stroke-width="1.1" stroke-dasharray="2 7" '
                     'stroke-linecap="round"/>'
                     % (_f(fin + 8), _f(cy), _f(min(x + pas, largeur)),
                        _f(cy), infere))
        x += pas
    o.append("</svg>")
    return "\n".join(o)


def schema(largeur=420.0, hauteur=300.0, fond=PANNEAU, mesure=ACCENT,
           infere=AMBRE, trait=DOUX):
    """Le schema qui prend la place d'une photographie.

    Une trajectoire de transfert : une orbite basse mesuree, une orbite
    haute mesuree, et entre les deux le segment de transfert en pointille,
    parce qu'il n'a pas encore ete parcouru. C'est deliberement abstrait, et
    c'est la meme convention que la marque.

    Il est pose a chaque emplacement ou une image viendra un jour, avec la
    phrase qui dit ce qui manque et a quelle condition elle arrivera.
    """
    cx = largeur * 0.42
    cy = hauteur * 0.52
    o = [_entete(largeur, hauteur, "Schema orbital")]
    o.append('<rect width="%s" height="%s" fill="%s"/>'
             % (_f(largeur), _f(hauteur), fond))
    o.append('<g fill="none" stroke-linecap="round">')
    o.append('<circle cx="%s" cy="%s" r="%s" stroke="%s" stroke-width="1.6" '
             'opacity="0.85"/>' % (_f(cx), _f(cy), _f(hauteur * 0.16), mesure))
    o.append('<circle cx="%s" cy="%s" r="%s" stroke="%s" stroke-width="1.6" '
             'opacity="0.6"/>' % (_f(cx), _f(cy), _f(hauteur * 0.34), mesure))
    o.append('<path d="%s" stroke="%s" stroke-width="2.2" '
             'stroke-dasharray="3 9"/>'
             % (arc(cx, cy, hauteur * 0.25, 205.0, 210.0), infere))
    o.append('<path d="M %s %s L %s %s" stroke="%s" stroke-width="1" '
             'opacity="0.4"/>'
             % (_f(largeur * 0.08), _f(hauteur * 0.86),
                _f(largeur * 0.92), _f(hauteur * 0.86), trait))
    o.append("</g>")
    o.append('<circle cx="%s" cy="%s" r="7" fill="%s"/>'
             % (_f(cx), _f(cy), mesure))
    o.append('<circle cx="%s" cy="%s" r="4" fill="%s"/>'
             % (_f(cx + hauteur * 0.34), _f(cy), infere))
    o.append("</svg>")
    return "\n".join(o)


def legende(largeur=300.0, hauteur=74.0, mesure=ACCENT, infere=AMBRE):
    """La convention, dessinee : trait plein = mesure, pointille = infere.

    Elle est posee une fois sur la page qui explique la ligne editoriale.
    Le texte qui l'accompagne est du VRAI texte a cote du SVG, jamais dans
    le SVG : un mot dessine dans une image ne se traduit pas, ne se
    selectionne pas et ne se lit pas a voix haute.
    """
    o = [_entete(largeur, hauteur, "Convention de trace")]
    o.append('<g fill="none" stroke-width="4" stroke-linecap="round">')
    o.append('<path d="M 12 24 L 118 24" stroke="%s"/>' % mesure)
    o.append('<path d="M 12 54 L 118 54" stroke="%s" '
             'stroke-dasharray="3 10"/>' % infere)
    o.append("</g></svg>")
    return "\n".join(o)


def ecrire():
    if not os.path.isdir(ACTIFS):
        os.makedirs(ACTIFS)
    fichiers = {
        "marque-accent.svg": marque(),
        "marque-clair.svg": marque(CLAIR, CLAIR, CLAIR),
        "marque-sombre.svg": marque(ACCENT_SOMBRE, AMBRE_SOMBRE,
                                    ACCENT_SOMBRE),
        "marque-duo.svg": marque(ACCENT, AMBRE, CLAIR),
        "favicon.svg": favicon(),
        "tuile.svg": tuile(),
        "frise.svg": frise(),
        "schema.svg": schema(),
        "legende.svg": legende(),
    }
    for nom, contenu in sorted(fichiers.items()):
        with open(os.path.join(ACTIFS, nom), "w", encoding="utf-8") as f:
            f.write(contenu + "\n")
        print("ecrit  assets/%s  (%d o)" % (nom, len(contenu) + 1))
    return len(fichiers)


if __name__ == "__main__":
    n = ecrire()
    print("%d fichiers d'ornement" % n)
