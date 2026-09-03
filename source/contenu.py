# -*- coding: utf-8 -*-
"""
Tout le texte du site, en francais et en anglais.

Chaque chaine est un COUPLE `(fr, en)`. Aucune phrase n'existe dans une
seule langue : une page a moitie traduite est pire qu'une page absente,
parce qu'elle a l'air finie.

LA REGLE DE CE CHANTIER, et elle vient de son chapitre 11 :

    On distingue le FAIT, l'HYPOTHESE, l'OPINION et la SPECULATION,
    et la distinction est VISIBLE, pas sous-entendue.

Pratiquement : aucun element scientifique n'est publie sans une etiquette
qui dit son statut. L'etiquette est un element d'interface, pas une nuance
de style — elle se lit a voix haute, elle survit a l'impression, et elle
existe encore quand la feuille de style ne se charge pas.

CE QUI N'EST PAS ECRIT ICI, ET NE DOIT JAMAIS L'ETRE :

* Aucun rendement, aucun chiffre de performance, aucune promesse de gain.
  Son chapitre 8 dit que la branche investissement « MAY operate as a
  future fund » : c'est un CONCEPT. Un fonds d'investissement est une
  activite reglementee, et ecrire qu'il existe deja serait faux dans tous
  les pays a la fois.
* Aucun nom d'expert, d'ingenieur, de chercheur, d'astronaute, de startup
  ou de partenaire. Le cahier des charges n'en donne aucun.
* Aucun nombre de membres, d'articles, de projets ou de contributeurs. Son
  chapitre 14 en fait des INDICATEURS A SUIVRE, pas des resultats acquis.
* Aucune date de mission, aucun resultat experimental, aucun chiffre
  d'observation. Ce site n'a pas de source pour les verifier.

MOT D'ATTENTE DE CE CHANTIER : « A valider » / « To be validated ».
Il ne se melange JAMAIS aux mots d'attente des autres chantiers du meme
client. Le controle le verifie.
"""

# ------------------------------------------------------------------ marque
# Le nom est UN DES SIX qu'il propose au chapitre 12. Il n'a pas tranche.
# On en affiche un pour que les pages soient lisibles, marque comme
# provisoire a trois endroits, et le choix reste entierement le sien.
MARQUE = ("Deep Orbit Network", "Deep Orbit Network")
BASELINE = ("Le fait, l'hypothese et ce qui reste a decouvrir",
            "Fact, hypothesis, and what remains to be found")
NOM_TRAVAIL = ("nom de travail", "working name")
NOM_TRAVAIL_LONG = (
    "« Deep Orbit Network » est l'un des six noms proposes au chapitre 12 du "
    "cahier des charges. Il est affiche pour que les pages soient lisibles, "
    "pas parce qu'il a ete retenu. Les cinq autres sont Orbital Forum, Space "
    "Frontier Lab, Cosmos R&D, Celestial Ventures et Universe Systems ; le "
    "choix n'appartient pas au site.",
    "“Deep Orbit Network” is one of the six names proposed in "
    "chapter 12 of the specification. It is shown so that the pages can be "
    "read, not because it has been chosen. The other five are Orbital Forum, "
    "Space Frontier Lab, Cosmos R&D, Celestial Ventures and Universe "
    "Systems; the choice does not belong to the site.")

ATTENTE = ("A valider", "To be validated")

LANGUE_AUTRE = ("English", "Français")

# ------------------------------------------------------------------ pages
# (dossier, fichier_fr, fichier_en, titre_fr, titre_en, menu_fr, menu_en)
PAGES = [
    ("index.html", "index.html",
     "Le fait, l'hypothèse et ce qui reste à découvrir",
     "Fact, hypothesis, and what remains to be found",
     "Accueil", "Home"),
    ("forum.html", "forum.html",
     "Le forum", "The forum", "Forum", "Forum"),
    ("mysteres-de-l-univers.html", "mysteries-of-the-universe.html",
     "Les mystères de l'univers", "Mysteries of the universe",
     "Mystères", "Mysteries"),
    ("fusees-et-lancement.html", "rockets-and-launch.html",
     "Fusées et systèmes de lancement", "Rockets and launch systems",
     "Fusées", "Rockets"),
    ("robotique-spatiale.html", "space-robotics.html",
     "Robotique spatiale", "Space robotics", "Robotique", "Robotics"),
    ("startups-et-investissement.html", "startups-and-investment.html",
     "Startups et investissement", "Startups and investment",
     "Startups", "Startups"),
    ("base-de-connaissances.html", "knowledge-base.html",
     "Base de connaissances", "Knowledge base", "Savoirs", "Knowledge"),
    ("ligne-editoriale.html", "editorial-standards.html",
     "Ligne éditoriale et modération", "Editorial standards and moderation",
     "Ligne éditoriale", "Standards"),
    ("feuille-de-route.html", "roadmap.html",
     "Feuille de route", "Roadmap", "Feuille de route", "Roadmap"),
    ("contact.html", "contact.html",
     "Contact", "Contact", "Contact", "Contact"),
    ("mentions-legales.html", "legal-notice.html",
     "Mentions légales", "Legal notice", None, None),
    ("confidentialite.html", "privacy.html",
     "Confidentialité", "Privacy", None, None),
    ("accessibilite.html", "accessibility.html",
     "Accessibilité", "Accessibility", None, None),
]

META = {
    "index.html": (
        "Plateforme d'innovation spatiale : forum, recherche, fusées, "
        "robotique et repérage de startups. Démonstration.",
        "Space innovation platform: forum, research, rockets, robotics and "
        "startup scouting. Demonstration."),
    "forum.html": (
        "Les dix catégories du forum, ses règles et son processus de "
        "modération, tels que définis au cahier des charges.",
        "The forum's ten categories, its rules and its moderation process, "
        "as defined in the specification."),
    "mysteres-de-l-univers.html": (
        "Trous noirs, matière noire, exoplanètes, signaux inexpliqués : "
        "chaque sujet porte le statut de ce qui en est dit.",
        "Black holes, dark matter, exoplanets, unexplained signals: every "
        "topic carries the status of what is said about it."),
    "fusees-et-lancement.html": (
        "Propulsion, lanceurs réutilisables, infrastructure de lancement et "
        "architecture de mission.",
        "Propulsion, reusable launchers, launch infrastructure and mission "
        "architecture."),
    "robotique-spatiale.html": (
        "Rovers, bras robotiques, navigation autonome et téléopération : la "
        "branche R&D, à l'état de concepts.",
        "Rovers, robotic arms, autonomous navigation and teleoperation: the "
        "R&D branch, at concept stage."),
    "startups-et-investissement.html": (
        "Les critères de repérage, et ce que la branche investissement est "
        "et n'est pas à ce stade.",
        "The scouting criteria, and what the investment branch is and is "
        "not at this stage."),
    "base-de-connaissances.html": (
        "Glossaire, chronologies, schémas et parcours d'apprentissage : la "
        "structure de la bibliothèque de référence.",
        "Glossary, timelines, diagrams and learning paths: the structure of "
        "the reference library."),
    "ligne-editoriale.html": (
        "Fait, hypothèse, opinion, spéculation : la convention qui gouverne "
        "chaque page du site.",
        "Fact, hypothesis, opinion, speculation: the convention that governs "
        "every page of this site."),
    "feuille-de-route.html": (
        "Les cinq phases du cahier des charges et les indicateurs de suivi, "
        "sans chiffre inventé.",
        "The five phases of the specification and the monitoring indicators, "
        "with no invented figure."),
    "contact.html": (
        "Écrire à la plateforme. Le formulaire est une maquette : il n'a pas "
        "encore de destinataire.",
        "Write to the platform. The form is a mock-up: it has no recipient "
        "yet."),
    "mentions-legales.html": (
        "Éditeur, hébergeur, statut juridique : ce qui reste à établir avant "
        "toute mise en ligne réelle.",
        "Publisher, host, legal status: what remains to be established "
        "before any real launch."),
    "confidentialite.html": (
        "Aucun cookie, aucune mesure d'audience, aucune requête sortante. Ce "
        "que cela veut dire exactement.",
        "No cookie, no analytics, no outgoing request. What that means "
        "exactly."),
    "accessibilite.html": (
        "Ce qui a été fait, ce qui est mesuré, et ce qui n'a pas pu être "
        "vérifié.",
        "What has been done, what is measured, and what could not be "
        "verified."),
}

# ------------------------------------------------------- statuts (chap. 11)
# Les quatre mots sont les SIENS. Ils ne sont ni traduits librement ni
# remplaces par des synonymes : c'est un vocabulaire, pas du style.
STATUTS = {
    "fait": (("Fait", "Fact"),
             ("Établi par l'observation ou la mesure, et non contesté dans "
              "la littérature scientifique.",
              "Established by observation or measurement, and not disputed "
              "in the scientific literature.")),
    "hypothese": (("Hypothèse", "Hypothesis"),
                  ("Explication proposée, compatible avec les observations, "
                   "mais pas encore tranchée.",
                   "A proposed explanation, consistent with observation, but "
                   "not yet settled.")),
    "opinion": (("Opinion", "Opinion"),
                ("Le jugement d'une personne identifiée, présenté comme tel.",
                 "The judgement of a named person, presented as such.")),
    "speculation": (("Spéculation", "Speculation"),
                    ("Extrapolation au-delà de ce que les données "
                     "permettent. Publiée uniquement si elle est signalée.",
                     "Extrapolation beyond what the data support. Published "
                     "only if it is flagged.")),
}

CONVENTION = (
    "Trait plein là où l'on a mesuré. Pointillé là où l'on n'a qu'inféré.",
    "Solid where something has been measured. Dashed where it has only "
    "been inferred.")

CONVENTION_TEXTE = (
    "C'est la marque, c'est le motif de fond, c'est la façon dont les "
    "schémas sont dessinés, et c'est la règle éditoriale. Le lecteur "
    "apprend la convention sur le logo et la retrouve partout ailleurs.",
    "It is the logo, it is the background motif, it is how the diagrams are "
    "drawn, and it is the editorial rule. A reader learns the convention "
    "from the logo and meets it everywhere else.")

# ------------------------------------------------------------------ accueil
ACC_TITRE = ("Le fait, l'hypothèse et ce qui reste à découvrir",
             "Fact, hypothesis, and what remains to be found")
ACC_CHAPO = (
    "Un forum sérieux, une plateforme de contenu scientifique, une base de "
    "connaissances, une branche de recherche en robotique et une structure "
    "de repérage de startups. Six branches, une seule règle : on dit "
    "toujours d'où l'on parle.",
    "A serious forum, a scientific media platform, a knowledge base, a "
    "robotics research branch and a startup scouting structure. Six "
    "branches, one rule: we always say where a statement stands.")

ACC_INTRO = (
    "Ce site est une démonstration bâtie sur le cahier des charges "
    "« All-in-One Space Innovation Platform ». Il montre la structure, la "
    "ligne éditoriale et la façon dont chaque affirmation portera son "
    "statut. Il ne contient encore ni article rédigé par un auteur "
    "identifié, ni startup référencée, ni membre.",
    "This site is a demonstration built on the “All-in-One Space "
    "Innovation Platform” specification. It shows the structure, the "
    "editorial line, and the way every statement will carry its status. It "
    "does not yet contain a single article by a named author, a listed "
    "startup, or a member.")

# (titre_fr, titre_en, texte_fr, texte_en, page)
ACC_BRANCHES = [
    ("Forum", "Forum",
     "Dix catégories, de la propulsion au droit spatial, avec des règles "
     "écrites et un processus de modération.",
     "Ten categories, from propulsion to space law, with written rules and "
     "a moderation process.",
     "forum.html"),
    ("Mystères de l'univers", "Mysteries of the universe",
     "Trous noirs, matière noire, exoplanètes, signaux inexpliqués. C'est "
     "la section où la convention compte le plus.",
     "Black holes, dark matter, exoplanets, unexplained signals. This is "
     "where the convention matters most.",
     "mysteres-de-l-univers.html"),
    ("Fusées et lancement", "Rockets and launch",
     "Propulsion, lanceurs réutilisables, infrastructure sol, mécanique "
     "orbitale, architecture de mission.",
     "Propulsion, reusable launchers, ground infrastructure, orbital "
     "mechanics, mission architecture.",
     "fusees-et-lancement.html"),
    ("Robotique spatiale", "Space robotics",
     "Rovers, bras robotiques, navigation autonome, téléopération. À "
     "l'état de concepts et d'études.",
     "Rovers, robotic arms, autonomous navigation, teleoperation. At "
     "concept and study stage.",
     "robotique-spatiale.html"),
    ("Startups et investissement", "Startups and investment",
     "Six critères de repérage, écrits avant tout dossier, et une branche "
     "financière qui reste un concept.",
     "Six scouting criteria, written before any application, and a "
     "financial branch that remains a concept.",
     "startups-et-investissement.html"),
    ("Base de connaissances", "Knowledge base",
     "Glossaire, chronologies, schémas, parcours d'apprentissage. Une "
     "bibliothèque durable plutôt qu'un fil d'actualité.",
     "Glossary, timelines, diagrams, learning paths. A durable library "
     "rather than a news feed.",
     "base-de-connaissances.html"),
]

ACC_PUBLICS_TITRE = ("À qui ce site s'adresse", "Who this site is for")
# (public_fr, public_en, besoin_fr, besoin_en)
ACC_PUBLICS = [
    ("Passionnés d'espace", "Space enthusiasts",
     "Des explications fiables, des débats, le suivi des missions.",
     "Reliable explanations, debate, mission updates."),
    ("Ingénieurs et chercheurs", "Engineers and researchers",
     "De la discussion technique et de la collaboration.",
     "Technical discussion and collaboration."),
    ("Startups", "Startups",
     "De la visibilité, des partenariats, un accès au financement.",
     "Visibility, partnerships, access to funding."),
    ("Investisseurs", "Investors",
     "Des dossiers triés et de l'analyse de secteur.",
     "Curated opportunities and sector analysis."),
    ("Étudiants", "Students",
     "Des guides, une orientation, une communauté.",
     "Guides, career orientation, a community."),
    ("Institutions", "Institutions",
     "Une cartographie de l'écosystème et des partenariats.",
     "Ecosystem mapping and partnerships."),
]

ACC_ETAT_TITRE = ("Ce que ce site est aujourd'hui",
                  "What this site is today")
ACC_ETAT = [
    ("C'est la phase 1 du cahier des charges : la marque, le plan du site, "
     "les catégories du forum et la ligne éditoriale.",
     "This is phase 1 of the specification: the brand, the site map, the "
     "forum categories and the editorial line."),
    ("Le forum n'a pas de comptes, pas de messages et pas de modérateurs. "
     "Les catégories et les règles sont écrites ; le logiciel ne l'est pas.",
     "The forum has no accounts, no posts and no moderators. The categories "
     "and the rules are written; the software is not."),
    ("Aucun article n'est signé, parce qu'aucun auteur n'est identifié. Ce "
     "qui est publié ici décrit l'état d'une question, jamais un résultat.",
     "No article is signed, because no author has been identified. What is "
     "published here describes the state of a question, never a result."),
    ("La branche investissement est un concept. Aucun fonds n'existe, "
     "aucun dossier n'est reçu, aucune somme n'est en jeu.",
     "The investment branch is a concept. No fund exists, no application is "
     "received, no money is involved."),
]

# ------------------------------------------------------------------- forum
FORUM_CHAPO = (
    "Un forum modéré pour discuter de fusées, de satellites, d'astronomie, "
    "de missions, de phénomènes inexpliqués et d'exploration future.",
    "A moderated community for discussing rockets, satellites, astronomy, "
    "missions, unexplained phenomena and future exploration.")

FORUM_CATEGORIES = [
    ("Fusées et propulsion", "Rockets and propulsion"),
    ("Agences spatiales et missions", "Space agencies and missions"),
    ("Satellites, télécoms et observation de la Terre",
     "Satellites, telecom and Earth observation"),
    ("Astronomie et découvertes lointaines",
     "Astronomy and deep-space discoveries"),
    ("Mystères de l'univers et hypothèses scientifiques",
     "Mysteries of the universe and scientific hypotheses"),
    ("Robotique spatiale et systèmes autonomes",
     "Space robotics and autonomous systems"),
    ("IA et logiciel pour les opérations spatiales",
     "AI and software for space operations"),
    ("Droit spatial, géopolitique et régulation",
     "Space law, geopolitics and regulation"),
    ("Idées de startups, brevets et opportunités d'investissement",
     "Startup ideas, patents and investment opportunities"),
    ("Projets étudiants, concours et éducation",
     "Student projects, competitions and education"),
]

FORUM_REGLES_TITRE = ("Les règles, écrites avant le premier message",
                      "The rules, written before the first post")
FORUM_REGLES = [
    ("Une affirmation scientifique porte son statut ou elle est reformulée. "
     "Ce n'est pas une politesse : c'est la condition pour que le désaccord "
     "soit possible.",
     "A scientific claim carries its status or it gets reworded. This is "
     "not a courtesy: it is what makes disagreement possible."),
    ("Une source vaut mieux qu'une certitude. Un message qui cite ce sur "
     "quoi il s'appuie est plus utile qu'un message qui a raison.",
     "A source beats a certainty. A post that cites what it rests on is "
     "more useful than a post that happens to be right."),
    ("Aucune sollicitation financière. Ni levée de fonds, ni placement, ni "
     "message privé proposant d'investir.",
     "No financial solicitation. No fundraising, no offer, no private "
     "message proposing an investment."),
    ("La spéculation est autorisée et signalée. On ne la censure pas, on "
     "l'étiquette.",
     "Speculation is allowed and flagged. It is not censored, it is "
     "labelled."),
    ("Les libellés d'expertise sont vérifiés ou ils n'existent pas. Un "
     "badge « ingénieur » que personne n'a contrôlé vaut moins que rien.",
     "Expert labels are verified or they do not exist. An “engineer” "
     "badge nobody checked is worse than none."),
    ("Attaquer un argument, jamais une personne.",
     "Attack an argument, never a person."),
]

FORUM_MODERATION_TITRE = ("Ce qui déclenche une relecture",
                          "What triggers a review")
FORUM_MODERATION = [
    ("Une affirmation technique présentée comme acquise sans source.",
     "A technical claim presented as settled without a source."),
    ("Un message qui touche à l'argent : levée, valorisation, rendement.",
     "A post touching money: fundraising, valuation, returns."),
    ("Une demande de libellé d'expertise.",
     "A request for an expert label."),
    ("Un signalement de désinformation par un autre membre.",
     "A misinformation report from another member."),
]

FORUM_ATTENTES = [
    ("Le logiciel de forum", "The forum software",
     "Comptes, messages, modération, profils : rien de tout cela n'est "
     "développé. Le choix entre un forum sur mesure et un moteur existant "
     "n'est pas tranché.",
     "Accounts, posts, moderation, profiles: none of it is built. The "
     "choice between a custom forum and an existing engine is open."),
    ("L'équipe de modération", "The moderation team",
     "Les règles ci-dessus n'ont de valeur que si quelqu'un les applique. "
     "Personne n'est désigné.",
     "The rules above are worth nothing unless someone applies them. "
     "Nobody is appointed."),
    ("La procédure de vérification des libellés",
     "The expert-label verification procedure",
     "Quelle preuve est demandée, qui la regarde, et combien de temps elle "
     "est conservée.",
     "What proof is asked for, who looks at it, and how long it is kept."),
]

# ---------------------------------------------------------------- mysteres
MYST_CHAPO = (
    "Trous noirs, matière noire, exoplanètes, origines cosmiques, temps, "
    "gravitation, signaux inexpliqués. C'est la section où la convention "
    "de ce site compte le plus, parce que c'est celle où l'on confond le "
    "plus facilement une question ouverte et une réponse.",
    "Black holes, dark matter, exoplanets, cosmic origins, time, gravity, "
    "unexplained signals. This is where this site's convention matters "
    "most, because it is where an open question is most easily mistaken "
    "for an answer.")

MYST_AVERT = (
    "Aucun résultat expérimental, aucune date d'observation et aucun "
    "chiffre ne sont publiés sur cette page. Ce qui suit décrit l'état de "
    "quelques questions et montre comment chaque élément portera son "
    "statut. Tout est en attente de relecture scientifique.",
    "No experimental result, no observation date and no figure is published "
    "on this page. What follows describes the state of a few questions and "
    "shows how each item will carry its status. All of it is awaiting "
    "scientific review.")

# (sujet_fr, sujet_en, [(statut, texte_fr, texte_en), ...])
MYST_SUJETS = [
    ("La matière noire", "Dark matter", [
        ("fait",
         "« Matière noire » est le nom donné à un écart : la masse déduite "
         "des effets gravitationnels ne coïncide pas avec la masse qu'on "
         "observe sous forme de lumière. L'écart, lui, est mesuré.",
         "“Dark matter” is the name given to a discrepancy: the "
         "mass inferred from gravitational effects does not match the mass "
         "observed as light. The discrepancy itself is measured."),
        ("hypothese",
         "Plusieurs familles d'explications coexistent — de nouvelles "
         "particules, ou une gravitation qui ne se comporte pas comme prévu "
         "à grande échelle. Aucune n'est tranchée. Le nom lui-même suppose "
         "déjà une réponse, ce qui est le piège de cette section.",
         "Several families of explanation coexist — new particles, or "
         "gravity not behaving as expected at large scale. None is settled. "
         "The name itself already assumes an answer, which is exactly the "
         "trap of this section."),
        ("speculation",
         "Tout ce qui va au-delà — « c'est forcément telle particule », « la "
         "gravitation est fausse » — appartient à cette catégorie et sera "
         "publié comme telle, jamais autrement.",
         "Anything beyond that — “it must be this particle”, "
         "“gravity is wrong” — belongs in this category and "
         "will be published as such, never otherwise."),
    ]),
    ("Les signaux inexpliqués", "Unexplained signals", [
        ("fait",
         "Des signaux dont l'origine n'a pas été établie sont enregistrés, "
         "publiés et réexaminés. Qu'un signal soit inexpliqué est une "
         "information sur l'état de l'analyse, pas sur sa source.",
         "Signals whose origin has not been established are recorded, "
         "published and re-examined. That a signal is unexplained is "
         "information about the state of the analysis, not about its "
         "source."),
        ("hypothese",
         "Une origine instrumentale, une origine terrestre et une origine "
         "astrophysique sont examinées avant toute autre, dans cet ordre, "
         "parce que c'est l'ordre de leur fréquence.",
         "An instrumental origin, a terrestrial origin and an "
         "astrophysical origin are examined before anything else, in that "
         "order, because that is the order of their frequency."),
        ("opinion",
         "La place à donner à ce sujet sur une plateforme grand public est "
         "un jugement éditorial, et il sera signé par la personne qui le "
         "porte.",
         "How much room to give this subject on a public platform is an "
         "editorial judgement, and it will be signed by whoever makes it."),
    ]),
    ("Le temps et la gravitation", "Time and gravity", [
        ("fait",
         "Le rythme d'une horloge dépend de son mouvement et du champ "
         "gravitationnel où elle se trouve. Ce n'est pas une curiosité "
         "théorique : les systèmes de navigation par satellite ne "
         "fonctionneraient pas si on l'ignorait.",
         "A clock's rate depends on its motion and on the gravitational "
         "field it sits in. This is not a theoretical curiosity: satellite "
         "navigation systems would not work if it were ignored."),
        ("hypothese",
         "La façon de faire tenir ensemble la gravitation et la physique "
         "quantique reste une question ouverte, avec plusieurs programmes "
         "de recherche concurrents.",
         "How to reconcile gravity with quantum physics remains an open "
         "question, with several competing research programmes."),
    ]),
]

MYST_ATTENTES = [
    ("La relecture scientifique", "Scientific review",
     "Aucun des textes ci-dessus n'a été relu par une personne qualifiée. "
     "Tant que ce n'est pas fait, ils décrivent une méthode, pas un savoir.",
     "None of the texts above has been reviewed by a qualified person. "
     "Until that happens, they demonstrate a method, not knowledge."),
    ("Les auteurs", "The authors",
     "Chaque élément portera le nom de qui l'écrit et de qui le relit. "
     "Aucun nom ne sera affiché sans accord écrit.",
     "Every item will carry the name of who writes it and who reviews it. "
     "No name will be shown without written agreement."),
    ("Les sources", "Sources",
     "Chaque « fait » renverra à une référence vérifiable. La page est "
     "construite pour les recevoir ; elles n'y sont pas encore.",
     "Every “fact” will point to a verifiable reference. The page "
     "is built to hold them; they are not there yet."),
]

# ------------------------------------------------------------------ fusees
FUS_CHAPO = (
    "Propulsion, lanceurs réutilisables, infrastructure de lancement, "
    "mécanique orbitale et architecture de mission.",
    "Propulsion, reusable launchers, launch infrastructure, orbital "
    "mechanics and mission architecture.")

FUS_TITRE = ("Les cinq domaines suivis", "The five areas covered")
FUS_SUJETS = [
    ("Propulsion", "Propulsion",
     "Chimique, électrique, nucléaire thermique : ce que chaque famille "
     "permet et ce qu'elle coûte en masse, en durée et en complexité.",
     "Chemical, electric, nuclear thermal: what each family makes possible "
     "and what it costs in mass, duration and complexity."),
    ("Réutilisation", "Reuse",
     "Ce qui est réutilisé, combien de fois, et à quelle condition la "
     "réutilisation est un gain plutôt qu'un coût déplacé.",
     "What is reused, how many times, and under what conditions reuse is a "
     "gain rather than a displaced cost."),
    ("Infrastructure sol", "Ground infrastructure",
     "Pas de tir, intégration, ravitaillement, contrôle : la partie la "
     "moins photographiée et souvent la plus contraignante.",
     "Pads, integration, propellant supply, control: the least "
     "photographed part, and often the most constraining."),
    ("Mécanique orbitale", "Orbital mechanics",
     "Transferts, fenêtres de tir, rendez-vous. C'est ici que le pointillé "
     "du schéma prend son sens : une trajectoire prévue n'est pas une "
     "trajectoire parcourue.",
     "Transfers, launch windows, rendezvous. This is where the dashed line "
     "in the diagram earns its meaning: a planned trajectory is not a "
     "flown one."),
    ("Architecture de mission", "Mission architecture",
     "Comment un objectif devient une suite d'étapes, et où se logent les "
     "hypothèses qu'on oublie d'écrire.",
     "How an objective becomes a sequence of steps, and where the "
     "assumptions nobody writes down end up hiding."),
]

FUS_ATTENTES = [
    ("Les données de référence", "Reference data",
     "Masses, poussées, cadences, coûts : aucun chiffre n'est publié tant "
     "qu'il n'a pas une source citable et une date de relevé.",
     "Masses, thrust, cadence, cost: no figure is published until it has a "
     "citable source and a date of record."),
    ("Les schémas techniques", "Technical diagrams",
     "Ils seront dessinés selon la convention du site, pas repris ailleurs. "
     "Un schéma trouvé sur internet appartient à quelqu'un.",
     "They will be drawn to the site's convention, not taken from "
     "elsewhere. A diagram found online belongs to someone."),
]

# --------------------------------------------------------------- robotique
ROB_CHAPO = (
    "La branche R&D explore des concepts et des prototypes de systèmes "
    "robotiques pour l'environnement spatial. Sa première phase est faite "
    "de simulation, d'études de conception, de petits prototypes et de "
    "partenariats avec des écoles d'ingénieurs ou des laboratoires.",
    "The R&D branch explores concepts and prototypes for robotic systems in "
    "space environments. Its first phase is simulation, design studies, "
    "small prototypes and partnerships with engineering schools or "
    "laboratories.")

ROB_AVERT = (
    "Tout ce qui suit est au stade du concept. Aucun prototype n'existe, "
    "aucun partenariat n'est signé, aucun laboratoire n'est engagé.",
    "Everything below is at concept stage. No prototype exists, no "
    "partnership is signed, no laboratory is committed.")

ROB_TITRE = ("Les sept axes explorés", "The seven areas explored")
ROB_AXES = [
    ("Rovers autonomes", "Autonomous rovers",
     "Concepts de mobilité pour terrain lunaire et planétaire.",
     "Mobility concepts for lunar and planetary terrain."),
    ("Bras robotiques", "Robotic arms",
     "Prélèvement d'échantillons, maintenance, assemblage.",
     "Sample collection, maintenance, assembly."),
    ("Navigation assistée par IA", "AI-assisted navigation",
     "Environnements peu visibles ou inconnus.",
     "Low-visibility or unknown environments."),
    ("Drones et micro-drones", "Drones and micro-drones",
     "Exploration en faible gravité.",
     "Low-gravity exploration."),
    ("Interfaces de téléopération", "Teleoperation interfaces",
     "Contrôle à distance, et ce que la latence impose à la conception.",
     "Remote control, and what latency imposes on the design."),
    ("Fusion de capteurs", "Sensor fusion",
     "Caméras, lidar, thermique et inertiel combinés.",
     "Cameras, lidar, thermal and inertial data combined."),
    ("Kits robotiques éducatifs", "Robotics education kits",
     "Pour les écoles, les universités et la démonstration publique.",
     "For schools, universities and public demonstration."),
]

ROB_ATTENTES = [
    ("Les partenaires académiques", "Academic partners",
     "Aucun établissement n'est cité tant qu'il n'a pas donné son accord "
     "écrit. Nommer une université qui n'a rien signé est une usurpation.",
     "No institution is named until it has given written agreement. Naming "
     "a university that signed nothing is a misrepresentation."),
    ("Les moyens", "Resources",
     "Atelier, budget, équipe : rien n'est arrêté, et la feuille de route "
     "en dépend entièrement.",
     "Workshop, budget, team: nothing is settled, and the roadmap depends "
     "entirely on it."),
]

# ---------------------------------------------------------------- startups
INV_CHAPO = (
    "Une structure de repérage, d'analyse et de soutien pour des sociétés "
    "d'aérospatiale, de robotique, de satellite et de deep-tech.",
    "A structure for scouting, analysing and supporting aerospace, "
    "robotics, satellite and deep-tech companies.")

# Le bloc le plus important du site. Il est en tete de page, pas en bas.
INV_AVERT_TITRE = ("Ce que cette branche n'est pas",
                   "What this branch is not")
INV_AVERT = [
    ("Aucun fonds n'existe. Le cahier des charges dit que la branche "
     "« pourra » fonctionner comme un fonds, un club de co-investissement, "
     "un accélérateur ou une cellule de repérage. Ces quatre formes ont des "
     "régimes juridiques différents, et aucune n'a été choisie.",
     "No fund exists. The specification says the branch “may” "
     "operate as a fund, a club deal structure, an accelerator or a "
     "scouting unit. Those four forms have different legal regimes, and "
     "none has been chosen."),
    ("Rien sur ce site n'est un conseil en investissement, une offre, une "
     "sollicitation, ni une invitation à investir.",
     "Nothing on this site is investment advice, an offer, a solicitation, "
     "or an invitation to invest."),
    ("Aucun rendement, aucune performance passée et aucune projection ne "
     "sera publiée. Pas même à titre d'illustration : un chiffre "
     "d'illustration se cite ensuite sans son étiquette.",
     "No return, no past performance and no projection will be published. "
     "Not even as an illustration: an illustrative figure gets quoted later "
     "without its label."),
    ("Aucun dossier n'est reçu par ce site. Le formulaire de contact est "
     "une maquette et n'a pas de destinataire.",
     "No application is received by this site. The contact form is a "
     "mock-up and has no recipient."),
    ("Une activité de gestion ou de placement est réglementée. Le régime "
     "applicable dépend du pays, qui reste à établir.",
     "Fund management and placement are regulated activities. The "
     "applicable regime depends on the country, which is yet to be "
     "established."),
]

INV_CRITERES_TITRE = ("Les six critères de repérage",
                      "The six scouting criteria")
INV_CRITERES_NOTE = (
    "Ils sont publiés avant d'avoir reçu le moindre dossier. Des critères "
    "écrits après coup s'ajustent toujours au dossier qu'on veut retenir.",
    "They are published before a single application has been received. "
    "Criteria written afterwards always end up fitting the application "
    "someone wanted to accept.")
INV_CRITERES = [
    ("Pertinence technique", "Technical relevance",
     "Le projet répond à un vrai problème d'aérospatiale, de robotique, de "
     "données ou d'infrastructure.",
     "The project solves a real aerospace, robotics, data or "
     "infrastructure problem."),
    ("Crédibilité scientifique", "Scientific credibility",
     "Les affirmations sont vérifiables et appuyées sur une expertise, un "
     "prototype ou des travaux publiés.",
     "Claims are verifiable and supported by expertise, a prototype or "
     "published work."),
    ("Potentiel de marché", "Market potential",
     "La société vise un besoin commercial ou institutionnel qui croît.",
     "The company targets a growing commercial or institutional need."),
    ("Solidité de l'équipe", "Team strength",
     "Capacité d'ingénierie, capacité d'exécution, clarté stratégique.",
     "Engineering ability, execution capacity, strategic clarity."),
    ("Potentiel de partenariat", "Partnership potential",
     "Le projet gagne à collaborer avec des laboratoires, des agences, "
     "l'industrie ou des investisseurs.",
     "The project benefits from collaboration with labs, agencies, "
     "industry or investors."),
    ("Défendabilité à long terme", "Long-term defensibility",
     "Technologie, données, brevets, savoir-faire ou complexité "
     "opérationnelle créent une barrière.",
     "Technology, data, patents, know-how or operational complexity create "
     "a barrier."),
]

INV_SECTEURS_TITRE = ("Les secteurs suivis", "Sectors followed")
INV_SECTEURS = [
    ("Infrastructure satellitaire et observation de la Terre",
     "Satellite infrastructure and Earth observation"),
    ("Lanceurs, propulsion et infrastructure sol",
     "Launch systems, propulsion and ground infrastructure"),
    ("Robotique spatiale et systèmes autonomes",
     "Space robotics and autonomous systems"),
    ("Logiciel et IA pour la planification et la télémétrie",
     "Software and AI for mission planning and telemetry"),
    ("Matériaux, capteurs, énergie et fabrication avancée",
     "Materials, sensors, energy and advanced manufacturing"),
    ("Logistique orbitale, services en orbite et suivi des débris",
     "Space logistics, orbital services and debris monitoring"),
    ("Éducation, simulation, formation et plateformes de données",
     "Education, simulation, training and space data platforms"),
]

INV_ATTENTES = [
    ("La forme juridique", "The legal form",
     "Fonds, club de co-investissement, accélérateur ou cellule de "
     "repérage. Ce choix commande tout le reste de la page.",
     "Fund, club deal, accelerator or scouting unit. This choice governs "
     "everything else on this page."),
    ("Le pays et le régulateur", "Country and regulator",
     "Les mentions obligatoires, les avertissements et l'accès réservé aux "
     "investisseurs qualifiés en dépendent.",
     "Mandatory disclosures, warnings and qualified-investor gating all "
     "depend on it."),
    ("La relecture juridique", "Legal review",
     "Cette page doit être relue par un professionnel du pays retenu avant "
     "toute mise en ligne réelle.",
     "This page must be reviewed by a professional in the chosen country "
     "before any real launch."),
    ("L'espace privé investisseurs", "The private investor area",
     "Le cahier des charges le prévoit. Il n'est pas construit : un espace "
     "réservé suppose des comptes, une vérification et une politique de "
     "conservation.",
     "The specification foresees it. It is not built: a gated area implies "
     "accounts, verification and a retention policy."),
]

# ------------------------------------------------------------------ savoirs
SAV_CHAPO = (
    "Une bibliothèque de référence plutôt qu'un fil d'actualité : "
    "glossaire, chronologies, schémas, explications et parcours "
    "d'apprentissage.",
    "A reference library rather than a news feed: glossary, timelines, "
    "diagrams, explainers and learning paths.")

SAV_TITRE = ("Les six formats publiés", "The six formats published")
SAV_TYPES = [
    ("Articles courts", "Short articles",
     "Expliquer clairement un sujet complexe.",
     "Explain a complex subject clearly."),
    ("Rapports longs", "Long reports",
     "Analyser une tendance ou une opportunité.",
     "Analyse a trend or an opportunity."),
    ("Débats du forum", "Forum debates",
     "Structurer l'intelligence de la communauté.",
     "Structure community intelligence."),
    ("Capsules vidéo", "Video capsules",
     "Toucher un public plus large.",
     "Reach a wider audience."),
    ("Entretiens", "Interviews",
     "Apporter la crédibilité de gens qui font le métier.",
     "Bring the credibility of people who do the work."),
    ("Base de connaissances", "Knowledge base",
     "Construire une référence durable.",
     "Build a durable reference."),
]

SAV_STRUCTURE_TITRE = ("Ce que la bibliothèque contiendra",
                       "What the library will hold")
SAV_STRUCTURE = [
    ("Un glossaire", "A glossary",
     "Chaque terme défini une fois, au même endroit, et lié depuis partout "
     "où il apparaît.",
     "Every term defined once, in one place, and linked from everywhere it "
     "appears."),
    ("Des chronologies", "Timelines",
     "Elles ne seront publiées qu'avec des dates sourcées. Une chronologie "
     "approximative est le format le plus recopié et le plus difficile à "
     "corriger ensuite.",
     "They will only be published with sourced dates. An approximate "
     "timeline is the most-copied format and the hardest to correct "
     "afterwards."),
    ("Des schémas", "Diagrams",
     "Dessinés selon la convention du site : plein pour le mesuré, "
     "pointillé pour l'inféré.",
     "Drawn to the site's convention: solid for measured, dashed for "
     "inferred."),
    ("Des parcours d'apprentissage", "Learning paths",
     "Un ordre de lecture, pour que la bibliothèque serve à quelqu'un qui "
     "commence.",
     "A reading order, so the library is usable by someone starting out."),
]

SAV_ATTENTES = [
    ("Les 20 premiers articles", "The first 20 articles",
     "La phase 1 du cahier des charges les prévoit. Ils demandent des "
     "auteurs identifiés et une relecture ; ni les uns ni l'autre "
     "n'existent.",
     "Phase 1 of the specification calls for them. They require named "
     "authors and a review process; neither exists yet."),
    ("Le moteur de recherche", "The search engine",
     "Une bibliothèque sans recherche n'est pas une bibliothèque. Elle "
     "suppose d'abord un format d'article arrêté.",
     "A library without search is not a library. It first requires a "
     "settled article format."),
]

# --------------------------------------------------------- ligne editoriale
LED_CHAPO = (
    "Le chapitre 11 du cahier des charges demande de distinguer le fait, "
    "l'hypothèse, l'opinion et la spéculation. Sur ce site, la distinction "
    "est un élément d'interface, pas une nuance de style.",
    "Chapter 11 of the specification asks to distinguish fact, hypothesis, "
    "opinion and speculation. On this site, that distinction is an "
    "interface element, not a matter of tone.")

LED_POURQUOI = (
    "Une étiquette de style — une couleur, une italique — disparaît quand "
    "la feuille de style ne se charge pas, quand la page est imprimée, "
    "quand elle est lue à voix haute, et quand un moteur en recopie un "
    "extrait. Les quatre cas sont exactement ceux où l'affirmation voyage "
    "le plus loin de son contexte. L'étiquette est donc du texte : elle "
    "reste lisible dans les quatre.",
    "A stylistic label — a colour, an italic — disappears when the "
    "stylesheet fails, when the page is printed, when it is read aloud, and "
    "when a search engine quotes an extract. Those four cases are exactly "
    "the ones where a claim travels furthest from its context. So the label "
    "is text: it survives all four.")

LED_REGLES_TITRE = ("Ce que la ligne éditoriale interdit",
                    "What the editorial line rules out")
LED_REGLES = [
    ("Le sensationnalisme. Le chapitre 6 demande un contenu sérieux et "
     "compréhensible ; un titre qui promet plus que le texte trahit les "
     "deux.",
     "Sensationalism. Chapter 6 asks for content that is serious and "
     "understandable; a headline promising more than the text betrays "
     "both."),
    ("Le ton complotiste. Un signal inexpliqué est une question ouverte, "
     "pas une dissimulation.",
     "A conspiracy register. An unexplained signal is an open question, "
     "not a cover-up."),
    ("La fausse science. Une affirmation sans source ne devient pas vraie "
     "parce qu'elle est bien écrite.",
     "Fake science. A claim without a source does not become true because "
     "it is well written."),
    ("Les promesses d'investissement exagérées, et toute promesse "
     "d'investissement en général.",
     "Exaggerated investment promises, and investment promises in "
     "general."),
    ("La spéculation non signalée. Signalée, elle a sa place.",
     "Unflagged speculation. Flagged, it has its place."),
]

LED_REVUE_TITRE = ("Le circuit de relecture", "The review process")
LED_REVUE = [
    ("Un rapport, une fiche de startup ou un article de recherche est relu "
     "avant publication.",
     "A report, a startup page or a research article is reviewed before "
     "publication."),
    ("Le relecteur est nommé sur la page, avec l'auteur.",
     "The reviewer is named on the page, alongside the author."),
    ("Une correction ne remplace pas silencieusement le texte : elle est "
     "datée et visible.",
     "A correction does not silently replace the text: it is dated and "
     "visible."),
    ("Un élément dont le statut change — d'hypothèse à fait, ou l'inverse — "
     "garde la trace du changement.",
     "An item whose status changes — from hypothesis to fact, or the "
     "reverse — keeps a record of the change."),
]

LED_ATTENTES = [
    ("Le comité de relecture", "The review board",
     "Aucun nom, aucune qualification et aucun titre ne sera affiché sans "
     "accord écrit et sans justificatif.",
     "No name, qualification or title will be shown without written "
     "agreement and supporting evidence."),
    ("La procédure de correction", "The correction procedure",
     "Qui peut signaler une erreur, sous quel délai elle est traitée, et où "
     "la correction apparaît.",
     "Who can report an error, within what delay it is handled, and where "
     "the correction appears."),
]

# ----------------------------------------------------------- feuille de route
FDR_CHAPO = (
    "Les cinq phases du chapitre 13, dans son ordre. Aucune date n'y est "
    "ajoutée : le cahier des charges n'en donne pas, et une date inventée "
    "sur une feuille de route devient un engagement dans la tête de celui "
    "qui la lit.",
    "The five phases of chapter 13, in its order. No date has been added: "
    "the specification gives none, and an invented date on a roadmap "
    "becomes a commitment in the mind of whoever reads it.")

# (n, titre_fr, titre_en, livrables_fr, livrables_en, etat)
FDR_PHASES = [
    ("Phase 1", "Concept et fondation du contenu",
     "Concept and content foundation",
     "Marque, plan du site, catégories du forum, 20 premiers articles.",
     "Brand, website map, forum categories, first 20 articles.",
     ("En cours", "In progress")),
    ("Phase 2", "Lancement de la communauté", "Community launch",
     "Forum, lettre d'information, profils de membres, règles de "
     "modération.",
     "Forum, newsletter, member profiles, moderation rules.",
     ("À venir", "Upcoming")),
    ("Phase 3", "Recherche et annuaire de startups",
     "Research and startup directory",
     "Base de connaissances, fiches de startups, rapports sectoriels.",
     "Knowledge base, startup profiles, sector reports.",
     ("À venir", "Upcoming")),
    ("Phase 4", "Branche R&D", "R&D branch",
     "Pages de projets, concepts de robotique, partenariats de prototypage.",
     "Project pages, robotics concepts, prototype partnerships.",
     ("À venir", "Upcoming")),
    ("Phase 5", "Structure d'investissement", "Investment structure",
     "Processus de repérage, espace investisseurs, documentation du fonds.",
     "Deal scouting process, private investor area, fund documentation.",
     ("À venir", "Upcoming")),
]

FDR_PHASE1_NOTE = (
    "Ce site couvre la première ligne de la phase 1 : la marque, le plan du "
    "site et les catégories du forum. Les 20 articles ne sont pas écrits, "
    "parce qu'ils demandent des auteurs identifiés et une relecture.",
    "This site covers the first line of phase 1: the brand, the site map "
    "and the forum categories. The 20 articles are not written, because "
    "they require named authors and a review process.")

FDR_IND_TITRE = ("Les indicateurs de suivi", "Monitoring indicators")
FDR_IND_NOTE = (
    "Ce sont les huit indicateurs du chapitre 14. Ils sont affichés sans "
    "valeur, et ce n'est pas un oubli : ce sont des choses à mesurer, pas "
    "des résultats déjà obtenus. Aucun chiffre n'apparaîtra ici avant "
    "d'avoir été relevé.",
    "These are the eight indicators of chapter 14. They are shown without "
    "values, and that is not an omission: they are things to measure, not "
    "results already achieved. No figure will appear here before it has "
    "been recorded.")
FDR_INDICATEURS = [
    ("Membres inscrits et contributeurs actifs",
     "Registered members and active contributors"),
    ("Qualité et crédibilité des discussions et des rapports",
     "Quality and credibility of discussions and reports"),
    ("Contributeurs experts, chercheurs et ingénieurs impliqués",
     "Expert contributors, researchers and engineers involved"),
    ("Startups référencées, examinées ou soutenues",
     "Startups listed, reviewed or supported"),
    ("Projets R&D lancés ou menés en partenariat",
     "R&D projects initiated or partnered"),
    ("Croissance et engagement de la lettre d'information",
     "Newsletter growth and engagement"),
    ("Intérêt des investisseurs et flux de dossiers qualifiés",
     "Investor interest and qualified deal flow"),
    ("Réputation comme référence sérieuse de l'innovation spatiale",
     "Reputation as a serious reference for space innovation"),
]

# ------------------------------------------------------------------ contact
CON_CHAPO = (
    "Le formulaire ci-dessous est une maquette. Il vérifie les champs dans "
    "le navigateur et s'arrête là : il n'existe ni domaine, ni adresse "
    "professionnelle, ni destinataire.",
    "The form below is a mock-up. It validates the fields in the browser "
    "and stops there: there is no domain, no professional address, and no "
    "recipient yet.")

CON_CHAMPS = {
    "nom": (("Nom", "Name"), ("", "")),
    "contact": (("Comment vous répondre", "How to reply to you"),
                ("Une adresse ou un identifiant. Rien n'est envoyé pour "
                 "l'instant.",
                 "An address or a handle. Nothing is sent for now.")),
    "sujet": (("Sujet", "Subject"), ("", "")),
    "message": (("Message", "Message"),
                ("N'y écrivez rien de confidentiel : ce formulaire est une "
                 "maquette et n'a pas de destinataire.",
                 "Do not write anything confidential here: this form is a "
                 "mock-up and has no recipient.")),
}

CON_SUJETS = [
    ("", ("Choisir un sujet", "Choose a subject")),
    ("forum", ("Le forum", "The forum")),
    ("contribution", ("Proposer une contribution",
                      "Propose a contribution")),
    ("startup", ("Présenter un projet", "Introduce a project")),
    ("recherche", ("Partenariat de recherche", "Research partnership")),
    ("autre", ("Autre", "Other")),
]

CON_CONSENTEMENT = (
    "Je comprends que ce formulaire est une maquette, qu'aucune donnée "
    "n'est envoyée et qu'aucune réponse ne suivra.",
    "I understand this form is a mock-up, that no data is sent and that no "
    "reply will follow.")

CON_SUCCES = (
    "Formulaire valide, et rien n'a été envoyé. La plateforme n'a pas "
    "encore de destinataire : ni domaine, ni adresse professionnelle. "
    "Ce message existe pour que tu voies le comportement du formulaire, "
    "pas pour te faire croire qu'un message est parti.",
    "Form valid, and nothing has been sent. The platform has no recipient "
    "yet: no domain, no professional address. This message exists so you "
    "can see how the form behaves, not to make you believe a message went "
    "out.")

CON_ERREUR_RESUME = ("Le formulaire n'a pas pu être validé :",
                     "The form could not be validated:")

CON_ATTENTES = [
    ("Le domaine", "The domain",
     "Il commande l'adresse professionnelle, le certificat et les liens "
     "canoniques.",
     "It governs the professional address, the certificate and the "
     "canonical links."),
    ("Le destinataire", "The recipient",
     "Une adresse relevée par quelqu'un. Sans elle, un formulaire qui "
     "prétend envoyer est un mensonge poli.",
     "An address someone actually reads. Without it, a form that claims to "
     "send is a polite lie."),
    ("Les canaux officiels", "Official channels",
     "Aucun compte de réseau social n'est lié tant qu'il n'est pas "
     "confirmé. Un lien vers un compte qui n'est pas le vôtre est une "
     "usurpation.",
     "No social account is linked until it is confirmed. A link to an "
     "account that is not yours is impersonation."),
]

# ---------------------------------------------------------------- juridique
MENT_CHAPO = (
    "Cette page est incomplète, et elle le restera tant que les décisions "
    "ci-dessous n'auront pas été prises. Une mention légale inventée est "
    "pire qu'une mention légale absente : elle a l'air valable.",
    "This page is incomplete, and it will stay that way until the decisions "
    "below have been made. An invented legal notice is worse than a missing "
    "one: it looks valid.")

MENT_ATTENTES = [
    ("L'éditeur", "The publisher",
     "Dénomination, forme juridique, adresse du siège, numéro "
     "d'immatriculation, directeur de la publication.",
     "Legal name, legal form, registered address, registration number, "
     "publication director."),
    ("Le pays", "The country",
     "Il détermine les mentions obligatoires, le régime de protection des "
     "données et le régulateur financier compétent.",
     "It determines the mandatory disclosures, the data protection regime "
     "and the competent financial regulator."),
    ("L'hébergeur", "The host",
     "Nom, raison sociale et adresse, exigés dans la plupart des pays.",
     "Name, company and address, required in most countries."),
    ("La propriété du nom", "Ownership of the name",
     "Le nom affiché est provisoire. Avant toute mise en ligne réelle, il "
     "doit être vérifié comme disponible, en tant que marque et en tant que "
     "domaine.",
     "The displayed name is provisional. Before any real launch it must be "
     "checked as available, both as a trademark and as a domain."),
]

CONF_CHAPO = (
    "Ce site de démonstration ne dépose aucun cookie, ne mesure aucune "
    "audience et n'envoie aucune requête vers un autre domaine. Ce ne sont "
    "pas des intentions : la vérification compte les requêtes de chaque "
    "page et exige zéro.",
    "This demonstration site sets no cookie, measures no audience and sends "
    "no request to any other domain. These are not intentions: the "
    "verification counts every page's requests and requires zero.")

CONF_FAITS = [
    ("Les polices sont servies depuis ce site. Une police chargée chez un "
     "tiers lui transmettrait l'adresse exacte de la page lue.",
     "Fonts are served from this site. A font loaded from a third party "
     "would hand it the exact address of the page being read."),
    ("Le formulaire de contact n'envoie rien et ne conserve rien. Ce qui "
     "est saisi ne quitte pas le navigateur.",
     "The contact form sends nothing and stores nothing. What is typed "
     "never leaves the browser."),
    ("Aucun compte, aucune inscription, aucun identifiant.",
     "No account, no sign-up, no identifier."),
    ("Le site fonctionne sans JavaScript, avec le menu et le formulaire "
     "utilisables.",
     "The site works without JavaScript, with the menu and the form still "
     "usable."),
]

CONF_ATTENTES = [
    ("Le responsable du traitement", "The data controller",
     "Dès qu'il y aura un forum, des comptes ou un espace investisseurs, "
     "il faudra une personne identifiée, une base légale et une durée de "
     "conservation.",
     "As soon as there is a forum, accounts or an investor area, there must "
     "be a named person, a legal basis and a retention period."),
    ("Le régime applicable", "The applicable regime",
     "Il dépend du pays, qui reste à établir.",
     "It depends on the country, which is yet to be established."),
]

ACCESS_CHAPO = (
    "Ce qui a été fait, ce qui est mesuré à chaque construction du site, et "
    "ce qui n'a pas pu être vérifié.",
    "What has been done, what is measured on every build, and what could "
    "not be verified.")

ACCESS_FAIT = [
    ("Contrastes mesurés dans un navigateur réel, pas déduits de la feuille "
     "de style. Le plus faible du site est indiqué dans le README.",
     "Contrast measured in a real browser, not derived from the "
     "stylesheet. The site's lowest value is given in the README."),
    ("Navigation au clavier : lien d'évitement, ordre de tabulation, "
     "contour de focus visible, menu qui s'ouvre et se ferme.",
     "Keyboard navigation: skip link, tab order, visible focus outline, a "
     "menu that opens and closes."),
    ("Les étiquettes de statut sont du texte, pas une couleur. Elles se "
     "lisent à voix haute et survivent à l'impression.",
     "Status labels are text, not a colour. They are read aloud and they "
     "survive printing."),
    ("Les schémas sont décoratifs et masqués aux lecteurs d'écran ; ce "
     "qu'ils illustrent est toujours écrit à côté en toutes lettres.",
     "Diagrams are decorative and hidden from screen readers; what they "
     "illustrate is always written out beside them."),
    ("Aucun défilement horizontal entre 320 et 1440 pixels, vérifié à "
     "chaque largeur de bascule.",
     "No horizontal scrolling between 320 and 1440 pixels, checked at every "
     "breakpoint."),
    ("Le mouvement réduit est respecté.",
     "Reduced motion is respected."),
]

ACCESS_PAS_FAIT = [
    ("Le site n'a pas été testé avec un lecteur d'écran par une personne "
     "qui en utilise un tous les jours. Les contrôles automatiques ne "
     "remplacent pas cet essai.",
     "The site has not been tested with a screen reader by someone who uses "
     "one daily. Automated checks do not replace that."),
    ("Aucune déclaration de conformité n'est publiée. Une déclaration "
     "suppose un audit, et il n'a pas eu lieu.",
     "No conformity statement is published. A statement implies an audit, "
     "and none has taken place."),
]

# ------------------------------------------------------------------ commun
DEMO_BANDEAU = (
    "Démonstration. Le nom, le pays et la forme juridique ne sont pas "
    "encore fixés, aucune page n'est indexée, et aucun fonds n'existe.",
    "Demonstration. The name, the country and the legal form are not yet "
    "settled, no page is indexed, and no fund exists.")

PIED_NOTE = (
    "Site de démonstration bâti sur le cahier des charges du client. Rien "
    "n'y est affirmé qui n'en vienne.",
    "Demonstration site built on the client's specification. Nothing is "
    "asserted here that does not come from it.")

ATTENTE_TITRE = ("Ce qui reste à valider", "What remains to be validated")
ALLER_PLUS = ("Lire la ligne éditoriale", "Read the editorial standards")
EVITEMENT = ("Aller au contenu", "Skip to content")
MENU = ("Menu", "Menu")
FIL = ("Vous êtes ici", "You are here")
