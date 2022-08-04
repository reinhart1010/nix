---
layout: page
title: common/atom (français)
description: "Un éditeur de texte multiplateforme proposant de nombreuses extensions."
content_hash: d5c960805d530692dfed41da6a23741efb4ac589
related_topics:
  - title: Deutsch version
    url: /de/common/atom.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/atom.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atom.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atom.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/atom.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atom.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/atom.html
    icon: bi bi-globe
---
# atom

Un éditeur de texte multiplateforme proposant de nombreuses extensions.
Les extensions sont gérées par `apm`.
Plus d'informations : <https://atom.io/>.

- Ouvrir un fichier ou un dossier :

`atom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_dossier</span>

- Ouvrir un fichier ou un dossier dans une nouvelle fenêtre :

`atom -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_dossier</span>

- Ouvrir un fichier ou un dossier dans une fenêtre existante :

`atom --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_dossier</span>

- Ouvrir en mode sans-échec (les extensions ne seront pas chargées) :

`atom --safe`

- Empêcher Atom de se lancer en arrière-plan, en le forçant à s'attacher au terminal :

`atom --foreground`

- Attendre la fermeture de la fenêtre avant de quitter (utile pour l'éditeur de commits Git) :

`atom --wait`
