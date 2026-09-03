# Plateforme d'innovation spatiale — site de démonstration

Site statique bilingue (français / anglais) bâti sur le cahier des charges
*All-in-One Space Innovation Platform*, fourni par le client. 26 pages
rendues, plus la page d'aiguillage, le plan de site et le `robots.txt`.

Aucun serveur, aucune base de données, aucune dépendance : des fichiers
HTML, une feuille de style, un script de 147 lignes, neuf ornements SVG et
une police servie depuis le site.

---

## La règle qui gouverne tout le reste

Elle vient de son chapitre 11, et elle est reprise mot pour mot :

> **On distingue le fait, l'hypothèse, l'opinion et la spéculation.**

Sur ce site, cette distinction est un **élément d'interface**, pas une
nuance de style. Chaque élément scientifique porte une étiquette écrite —
`Fait`, `Hypothèse`, `Opinion`, `Spéculation` — et cette étiquette est du
**texte**, jamais une couleur seule.

La raison est mesurable. Une étiquette de style — une couleur, une
italique — disparaît dans quatre cas : quand la feuille de style ne se
charge pas, quand la page est imprimée, quand elle est lue à voix haute, et
quand un moteur en recopie un extrait. Ce sont exactement les quatre cas où
l'affirmation voyage le plus loin de son contexte. La vérification teste
les deux premiers explicitement (sections 11 et 12).

### La convention de tracé

> **Trait plein là où l'on a mesuré. Pointillé là où l'on n'a qu'inféré.**

C'est la marque, c'est le motif de fond, c'est la façon dont les schémas
sont dessinés, et c'est la règle éditoriale. Le lecteur apprend la
convention sur le logo, la relit en haut de chaque page, et la retrouve
partout ailleurs.

---

## Ce qui n'est pas sur le site, et pourquoi

| Absence | Raison |
|---|---|
| **Aucun rendement, aucune performance, aucune projection** | Une activité de gestion ou de placement est réglementée. Un chiffre publié à titre d'illustration se cite ensuite sans son étiquette. |
| **Aucune affirmation qu'un fonds existe** | Son chapitre 8 dit que la branche « *may* operate as a future fund, club deal structure, accelerator or strategic scouting unit ». Ces quatre formes ont des régimes juridiques différents et aucune n'a été choisie. C'est un concept, et la page le dit en tête. |
| **Aucun nom d'expert, de chercheur, d'astronaute, de startup ou de partenaire** | Le cahier des charges n'en donne aucun. Nommer un laboratoire qui n'a rien signé est une usurpation. |
| **Aucun nombre de membres, d'articles ou de projets** | Son chapitre 14 en fait des *indicateurs à suivre*, pas des résultats acquis. Ils sont affichés sans valeur — et pas avec un zéro, parce qu'un zéro est une mesure et personne n'a mesuré. |
| **Aucun nom d'agence ou de lanceur réel** | NASA, ESA, SpaceX, Ariane : ce site n'a aucun lien avec elles. Le contrôle refuse ces mots, et il refuse aussi leurs logos. |
| **Aucune photographie** | Ni de mission, ni de fusée, ni de personne. Une photo de lancement appartient presque toujours à une agence ou à un industriel, et une image de nébuleuse « générique » sous un titre précis affirme un fait que personne n'a vérifié. |
| **Aucun résultat expérimental, aucune date d'observation, aucun chiffre** | Ce site n'a pas de source pour les vérifier. |

Ces absences ne sont pas des intentions : elles sont **vérifiées
mécaniquement** sur les 26 pages rendues. Voir « Vérification ».

### Le mot d'attente

Là où quelque chose manque, la page porte **« À valider » / « To be
validated »**, accompagné de la **condition exacte** qui le lèvera. Un
manque sans sa condition ressemble à un oubli ; avec sa condition, c'est
une décision qui attend quelqu'un.

---

## Le nom affiché est un nom de travail

Son chapitre 12 propose six noms et n'en retient aucun. Le site affiche
**Deep Orbit Network**, marqué comme nom de travail à trois endroits :
sous le nom dans l'en-tête, dans le pied de page, et dans le bandeau de
démonstration.

Ce n'est pas une proposition déguisée en décision — c'est un nom qui
permet de lire les pages en attendant la sienne. Les cinq autres (Orbital
Forum, Space Frontier Lab, Cosmos R&D, Celestial Ventures, Universe
Systems) sont rappelés dans le pied de page.

Il tient dans une seule constante, `MARQUE`, dans `source/contenu.py`.

---

## Le symbole

Une orbite **pleine** sur la portion observée, **pointillée** sur la
portion qui ne l'a pas été, et un corps plein au centre — la seule chose
dont l'existence n'est pas en discussion.

Le pointillé n'est pas un ornement. Il est de la **même épaisseur** que le
plein, pour qu'on lise « même trajectoire, statut différent » et non
« trait principal et trait secondaire ».

Tout est produit par `source/motif.py` à partir d'une seule fonction,
`arc(cx, cy, r, début, étendue)`. C'est l'**étendue** qui est le paramètre,
parce que c'est elle qui dit quelle part de l'orbite a été observée :
la régler, c'est régler le rapport entre le mesuré et l'inféré, et c'est le
seul réglage de cette marque qui change ce qu'elle raconte.

Deux réglages faits en regardant le rendu, pas le code :

* **Le favicon.** À 32 px, un `stroke-dasharray` de 2 sur 17 se lit comme
  une ligne sale ou comme rien du tout. Les tirets y sont
  proportionnellement plus gros et moins nombreux : trois interruptions
  franches valent mieux que douze invisibles.
* **Le motif de fond.** Rayon à 0,38 fois le côté de la tuile et non la
  moitié : à la moitié exacte, les cercles voisins se coupent au milieu de
  chaque bord et dessinent une file d'ogives pointues.

Les noms de fichiers sont neutres — `marque-accent`, `marque-clair`,
`marque-sombre`, `marque-duo` — et pas des noms de couleur. Sur le chantier
précédent la palette a changé en cours de route ; des fichiers nommés
d'après une teinte auraient forcé à renommer partout.

---

## Les 26 pages

Son chapitre 10 fixe les fonctionnalités, son chapitre 13 fixe les phases.
Ce site couvre la **phase 1** : marque, plan du site, catégories du forum
et ligne éditoriale.

| Page | Français | Anglais |
|---|---|---|
| Accueil | `fr/index.html` | `en/index.html` |
| Forum | `forum.html` | `forum.html` |
| Mystères de l'univers | `mysteres-de-l-univers.html` | `mysteries-of-the-universe.html` |
| Fusées et lancement | `fusees-et-lancement.html` | `rockets-and-launch.html` |
| Robotique spatiale | `robotique-spatiale.html` | `space-robotics.html` |
| Startups et investissement | `startups-et-investissement.html` | `startups-and-investment.html` |
| Base de connaissances | `base-de-connaissances.html` | `knowledge-base.html` |
| Ligne éditoriale | `ligne-editoriale.html` | `editorial-standards.html` |
| Feuille de route | `feuille-de-route.html` | `roadmap.html` |
| Contact | `contact.html` | `contact.html` |
| Mentions légales | `mentions-legales.html` | `legal-notice.html` |
| Confidentialité | `confidentialite.html` | `privacy.html` |
| Accessibilité | `accessibilite.html` | `accessibility.html` |

### Le forum n'est pas un forum

Les dix catégories, les six règles et les quatre déclencheurs de relecture
sont écrits. Le logiciel ne l'est pas : ni comptes, ni messages, ni
modérateurs. La page le dit en toutes lettres plutôt que de laisser croire
qu'on peut s'inscrire.

Les règles sont publiées **avant** le premier message, et les six critères
de repérage **avant** le premier dossier. Des critères écrits après coup
s'ajustent toujours au dossier qu'on voulait retenir.

### L'avertissement financier est en tête de page

Sur la page Startups et investissement, le bloc « Ce que cette branche
n'est pas » est placé **avant** le contenu qu'il corrige. Un avertissement
placé en bas de page n'est pas lu par ceux qu'il devrait protéger.

### Le formulaire n'envoie rien, et il le dit

Il valide les champs dans le navigateur et s'arrête là : il n'existe ni
domaine, ni adresse professionnelle, ni destinataire. Le message affiché
après une validation réussie dit exactement cela, et il ne propose **aucune
adresse ni aucun numéro de repli** — il n'en existe pas, et en inventer un
serait précisément la faute que tout le reste du site évite. La
vérification cherche une adresse et un numéro dans ce message et exige de
n'en trouver aucun.

---

## Vérification

```
python3 -m http.server 8875 --bind 127.0.0.1   # depuis la racine du site
python3 tests/verif.py http://127.0.0.1:8875/
```

**2 583 contrôles, 0 échec.** Quatorze sections, sur les 26 pages rendues
et à 21 largeurs d'écran de 320 à 1440 pixels.

Lire la source dit ce qui a été écrit ; mesurer le rendu dit ce que le
navigateur a fait. Les contrastes, les débordements, les ancres, les
requêtes réseau et le comportement du formulaire sont donc mesurés dans un
Chromium réel, jamais déduits de la feuille de style.

Les largeurs testées encadrent **chaque** point de bascule de la feuille de
style (619/621, 799/801, 959/961, 1059/1061). Une règle qui ne se trompe
qu'à l'intérieur d'une bande étroite ne peut donc pas se cacher entre deux
mesures.

### Contrastes mesurés

Le texte est rendu transparent, la zone est photographiée, et l'on retient
le pixel de fond le plus défavorable (2ᵉ centile du **contraste**, pas de la
luminance). Cacher l'élément entier découvrirait le fond de son **ancêtre**,
ce qui donne une lecture fausse pour tout ce qui peint son propre fond.

| Élément | Largeur | Mesuré |
|---|---|---|
| Titre du héros | 1280 | 16,07:1 |
| Titre du héros | 390 | 16,07:1 |
| Chapô du héros | 1280 | 8,81:1 |
| Bandeau de démonstration | 1280 | 14,46:1 |
| Mention de la convention | 1280 | 8,81:1 |
| Bascule de langue | 1280 | 11,32:1 |
| Mention « nom de travail » | 1280 | 10,31:1 |
| Lien de menu | 1280 | 9,99:1 |
| Texte de carte | 1280 | 8,81:1 |
| Lien du pied de page | 1280 | 8,81:1 |
| Note du pied de page | 1280 | 8,81:1 |
| Étiquette « Fait » | 1280 | 7,46:1 |
| Étiquette « Hypothèse » | 1280 | 8,24:1 |
| Étiquette « Spéculation » | 1280 | 8,57:1 |
| Texte d'item scientifique | 1280 | 17,50:1 |
| Encart d'avertissement | 1280 | 16,07:1 |
| Avertissement financier | 1280 | 16,07:1 |
| Numéro de phase | 1280 | 8,81:1 |
| Badge « À valider » | 1280 | **6,70:1** |
| Libellé d'indicateur | 1280 | 16,07:1 |
| Aide de champ | 1280 | 9,59:1 |
| Fil d'Ariane | 1280 | 9,59:1 |

Le seuil retenu est 4,5:1. Le plus faible du site est **6,70:1**.

Les bordures des **contrôles** (champs, boutons, bascule de langue) sont
tenues séparément à 3:1, parce qu'une bordure ne porte pas de texte mais
dessine la limite d'un composant. La première valeur essayée, `#33445E`,
mesurait 2,00:1 : je l'avais calculée de tête au lieu de la calculer tout
court. La valeur retenue, `#406886`, mesure 3,32:1 sur le fond de nuit et
3,05:1 sur les panneaux.

### La mesure de contraste a un témoin

Chaque mesure photographie la zone **deux fois** — texte visible, puis
texte transparent — et exige que les deux images **diffèrent**. Si elles
sont identiques, la mesure ne regarde pas le texte : soit le cadrage vise
ailleurs, soit la mise en transparence n'a pas pris, et le chiffre qui
suivrait serait inventé.

Ce témoin n'est pas décoratif. La première version de cette suite ajoutait
`window.scrollY` au cadrage, parce que je croyais le cadrage relatif au
document ; il est relatif à la **fenêtre**. Le résultat n'a pas été une
erreur franche mais des **mesures fausses** : la capture photographiait une
zone située un écran plus bas et rapportait 1,02:1 pour un texte à 8,81:1.
Les éléments au-dessus de la ligne de flottaison, eux, mesuraient juste —
les deux lectures coïncident quand le défilement vaut zéro. Huit « échecs
de contraste » accusaient le site d'un défaut qui était dans l'instrument.

### Ce que la vérification contrôle

1. Structure : doctype, langue, un seul `h1`, lien d'évitement, canonique,
   trois `hreflang`, `noindex`, favicon, longueur des descriptions, absence
   de tout outil de mesure, absence de données structurées, nom marqué
   comme provisoire, convention énoncée sur chaque page.
2. Aucune ressource tierce, et **aucune image qui ne soit un des neuf
   ornements produits par `motif.py`** — une photographie ne peut pas
   entrer sans faire échouer ce contrôle.
3. Les motifs interdits : pourcentages, années, montants, téléphones,
   adresses électroniques, chiffres de fréquentation, noms d'agences et de
   lanceurs réels, rendements, performances, garanties, conseil en
   investissement, fonds présenté comme existant, superlatifs,
   sensationnalisme — en tenant compte des **phrases négatives**, parce
   qu'interdire le mot « rendement » interdirait aussi l'avertissement qui
   dit qu'aucun rendement ne sera publié.
4. Le mot d'attente est celui de ce chantier, et le vocabulaire d'attente
   des autres chantiers du même client ne sert jamais d'étiquette ici.
5. Les statuts du chapitre 11 : **un statut par élément scientifique**, les
   quatre définis sur la page Ligne éditoriale, et le mot écrit en toutes
   lettres.
6. Liens morts, aller-retour de langue, plan de site, `robots.txt`.
7. Rendu : erreurs console, requêtes hors domaine, images cassées,
   hiérarchie des titres, débordement horizontal à 21 largeurs.
8. Ancres sous l'en-tête collant, à 390 et 1280.
9. Clavier : tabulation, lien d'évitement, contour de focus, ouverture et
   fermeture du menu, `Échap`, cohérence de `aria-expanded` au-delà du
   point de bascule.
10. Formulaire : erreurs annoncées, une entrée par champ fautif, le lien
    d'erreur **donne le focus** au lieu de seulement faire défiler, aucun
    message de succès quand il est invalide, message honnête quand il est
    valide, **aucune adresse ni numéro inventé** dans ce message,
    consentement jamais coché d'avance, champ libre borné, `autocomplete`
    désactivé.
11. **Sans JavaScript** : le menu reste visible et le bouton reste caché,
    le pied liste les treize pages, le formulaire est utilisable, et les
    étiquettes de statut restent lisibles.
12. **Sans feuille de style** : les mots `Fait`, `Hypothèse` et
    `Spéculation` restent lisibles. C'est tout l'intérêt d'en avoir fait du
    texte.
13. Contrastes mesurés, avec le témoin décrit plus haut.
14. Mouvement réduit, impression en fond clair, et étiquettes qui
    survivent à l'impression.

### Le menu ne peut pas se refermer sur le lecteur

Le repli du menu est conditionné à une classe `js` que le script pose
lui-même. Sans JavaScript, **rien ne peut rouvrir un menu replié** : le
bouton n'a pas de gestionnaire, et la navigation serait purement et
simplement perdue sur mobile. Tant que la classe n'est pas là, le menu
s'affiche en liste et le bouton reste caché.

C'est ceinture et bretelles : le pied de page liste de toute façon les
treize pages sur chaque page, donc même un script à moitié chargé laisse le
site entièrement navigable.

### Mutations

Un contrôle qui n'a jamais échoué n'a rien prouvé. Onze défauts ont été
introduits un par un, chacun avec **sa propre preuve de rendu** à **sa
propre largeur**.

| Défaut introduit | Largeur | Preuve au rendu | Échecs |
|---|---|---|---|
| Une promesse de rendement | 1280 | « 12 % » est dans la page | 2 |
| Le fonds présenté comme existant | 1280 | « Notre fonds » est dans la page | 1 |
| Le nom d'une agence réelle | 1280 | « NASA » est dans la page | 2 |
| Un item scientifique sans étiquette | 1280 | 0 élément `.statut` | 10 |
| L'étiquette réduite à une couleur | 1280 | le mot fait 0 caractère | 5 |
| Une photographie de personne | 1280 | `src` vaut `equipe-ingenieurs.jpg` | 4 |
| Une police chargée chez un tiers | 1280 | 1 `<link>` vers `fonts.googleapis` | 78 |
| Menu piégé sans JavaScript | 390 | le bouton s'affiche (`block`) | 2 |
| Ancre sous l'en-tête collant | 390 | `scroll-margin-top` à `0px` | 2 |
| Minimum de grille en pixels durs | 320 | colonne de `340px` dans une boîte de 284 | 4 |
| Un texte secondaire sous le seuil | 1280 | couleur `rgb(58, 70, 88)` | 9 |
| *Restauration* | — | — | **0 sur 2 582** |

Le banc compare l'empreinte des quatre fichiers source **avant et après**
chaque mutation, et écrit `ecrit`, `INERTE` ou `BUILD-KO` sur la ligne. Les
onze lignes ci-dessus portent `ecrit`.

Ces trois états ne sont pas décoratifs — la première exécution en a produit
deux qui n'étaient pas `ecrit`, et les deux racontaient quelque chose :

* **Une mutation cassait le générateur.** Elle retirait un `%s` d'un
  gabarit ; les fichiers source changeaient donc bien, le garde-fou disait
  `ecrit`, mais le build échouait et les pages rendues restaient
  identiques. Le banc lit maintenant le code de retour du build, et cette
  ligne s'écrit `BUILD-KO`. C'est la preuve de rendu qui l'a signalée la
  première : elle rapportait un mot de 4 caractères là où la mutation
  aurait dû en laisser 0.
* **Une mutation traversait sans être vue** — celle qui écrivait « Notre
  fonds finance déjà des sociétés ». La cause était dans le contrôle, pas
  dans le site, et elle est décrite juste en dessous.

### Deux défauts trouvés dans le contrôle lui-même

Ils méritent d'être écrits, parce que dans les deux cas le contrôle
annonçait « tout va bien » et se trompait.

1. **Les marqueurs de négation étaient cherchés en sous-chaînes.** La règle
   « un rendement n'est interdit que dans une phrase affirmative » a besoin
   de reconnaître une négation ; elle cherchait `"ne "`, et `"ne "` se
   trouve dans **« Ligne éditoriale »**, un libellé du menu présent sur
   toutes les pages. N'importe quelle phrase pouvait donc passer pour une
   négation. Les marqueurs sont maintenant cherchés en **mots entiers**.
2. **Les phrases n'avaient pas de frontières.** Le texte était extrait en
   supprimant les balises, ce qui collait le menu, le fil d'Ariane et le
   titre en une seule « phrase » de trois cents caractères — rien de tout
   cela ne se termine par un point. La fenêtre examinée autour d'un motif
   interdit avalait donc la moitié de l'en-tête. Chaque fin de bloc devient
   maintenant une fin de phrase.

Ces deux défauts se renforçaient : une phrase trop longue avait d'autant
plus de chances de contenir un faux marqueur de négation. Il a fallu une
mutation pour les mettre au jour, et c'est exactement à cela qu'un banc de
mutation sert.

Une troisième correction, du même genre : `getComputedStyle(null)` lève une
exception et emporte toute la suite. Quand une mutation retirait les
étiquettes de statut, la suite ne rapportait pas dix échecs mais une pile
d'appels, que le banc enregistrait comme `-1`, c'est-à-dire comme rien du
tout. Un élément absent produit désormais **un échec nommé**.

### Un défaut que seule la démo en ligne a montré

La suite passait en local et échouait une fois publiée, sur un seul point :
sans JavaScript, à 390 px, le bouton de menu était mesuré à `inline-block`
au lieu de `none` — c'est-à-dire la valeur par défaut d'un `<button>`,
celle qu'il porte quand **aucune** feuille de style ne s'applique encore.

Le contrôle lisait la page après `domcontentloaded` et une temporisation
fixe de 120 ms. En local c'était suffisant ; à travers le réseau, non. Le
site n'avait rien. Le contrôle attend maintenant une propriété qui ne peut
venir que de la feuille de style — le fond bleu nuit du corps — avant de
mesurer quoi que ce soit, et c'est un contrôle de plus.

C'est la raison pour laquelle la suite est relancée **contre la démo
publiée**, et pas seulement contre le serveur local.

---

## Ce qui bloque la mise en ligne

Aucune de ces décisions ne m'appartient, et chacune est signalée sur la
page concernée.

| # | Décision | Ce qu'elle commande |
|---|---|---|
| S-01 | Le nom retenu parmi les six | Il est sur les vingt-six pages, dans les titres et dans le plan de site. Il doit aussi être vérifié comme disponible, en marque et en domaine. |
| S-02 | Le pays | Les mentions obligatoires, le régime de protection des données, et surtout le **régulateur financier** compétent. |
| S-03 | La forme de la branche investissement | Fonds, club de co-investissement, accélérateur ou cellule de repérage. Ce choix commande toute la page, et il est réglementé. |
| S-04 | Une relecture juridique | La page investissement doit être relue par un professionnel du pays retenu avant toute mise en ligne réelle. |
| S-05 | Le forum : logiciel ou vitrine | Un vrai forum suppose comptes, modération, conservation des données et une équipe. La phase 1 n'en a pas besoin. |
| S-06 | L'équipe de modération | Les règles écrites ne valent que si quelqu'un les applique. |
| S-07 | Le comité de relecture scientifique | Aucun nom, aucune qualification et aucun titre ne sera affiché sans accord écrit et sans justificatif. |
| S-08 | Le domaine et le destinataire | Sans eux, le formulaire n'a pas de destinataire. |
| S-09 | Les partenaires académiques | Aucun établissement n'est cité tant qu'il n'a pas donné son accord écrit. |
| S-10 | Les canaux officiels | Aucun compte n'est lié tant qu'il n'est pas confirmé. Un lien vers un compte qui n'est pas le vôtre est une usurpation. |
| S-11 | Les 20 premiers articles | Ils demandent des auteurs identifiés et un circuit de relecture. |

---

## Notes techniques

* **Démonstration.** `DEMO = True` dans `source/build.py` pose le bandeau,
  la balise `noindex` sur chaque page et un `robots.txt` fermé. Les trois
  ensemble, parce qu'un `robots.txt` n'empêche pas l'indexation d'une URL
  déjà connue. Le passer à `False` retire les trois d'un coup.
* **Aucune donnée structurée.** Déclarer une `Organization` dont le nom est
  un nom de travail, sans pays, sans adresse et sans forme juridique,
  publie une identité qui n'existe pas. Le problème est pire ici que sur un
  site ordinaire : le cahier des charges parle d'un fonds d'investissement,
  et une fiche auprès d'un moteur est précisément ce qui ferait croire
  qu'il existe.
* **Police servie depuis le site** (Inter, licence SIL OFL incluse dans
  `assets/fonts/`). Une police chargée chez un tiers lui transmettrait
  l'adresse exacte de la page lue. Les libellés techniques utilisent la
  pile monospace du système, qui ne coûte aucun téléchargement.
* **Aucun cookie, aucune mesure d'audience, aucune requête sortante.** Ce
  n'est pas une intention : le contrôle compte les requêtes de chaque page
  et exige zéro.
* **La page d'aiguillage ne choisit pas la langue.** Une redirection
  automatique sur `navigator.language` envoie un francophone sur la version
  anglaise dès qu'il emprunte un navigateur. Deux liens, égaux.
* **L'impression bascule en fond clair.** Imprimer un aplat bleu nuit vide
  une cartouche et rend le texte moins lisible, pas plus. Les étiquettes de
  statut restent, en noir sur blanc.

## Régénérer

```
python3 source/motif.py     # les 9 ornements SVG
python3 source/build.py     # les 26 pages + aiguillage + sitemap + robots
python3 tests/verif.py http://127.0.0.1:8875/
python3 tests/captures.py http://127.0.0.1:8875/
```

Les fichiers de `assets/` produits par `motif.py` et les pages produites
par `build.py` ne se modifient pas à la main : ils seraient écrasés au
prochain passage.

## Pour la personne qui relira le juridique

Selon le pays retenu, à examiner en priorité : le régime applicable à la
sollicitation et au placement auprès d'investisseurs, et ce qui distingue
un fonds d'un club de co-investissement et d'un accélérateur ; les
obligations d'information et de mise en garde ; l'accès réservé aux
investisseurs qualifiés ; le régime de protection des données personnelles
dès qu'il y aura des comptes ; la responsabilité de l'éditeur sur les
contenus publiés par des membres ; et les mentions obligatoires d'un site
d'édition.
