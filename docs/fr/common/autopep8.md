---
layout: page
title: common/autopep8 (français)
description: "Formate du code Python en accord avec le style PEP 8."
content_hash: 254cf863dbc5565396b39b0ff22a1502c0136565
related_topics:
  - title: English version
    url: /en/common/autopep8.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/autopep8.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># autopep8

Formate du code Python en accord avec le style PEP 8.
Plus d'informations : <https://github.com/hhatto/autopep8>.

- Formate une fichier vers la sortie standard, avec une taille de ligne maximal personnalisée :

`autopep8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.py</span>` --max-line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">longueur</span>

- Formate un fichier, en affichant les changements :

`autopep8 --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Formate un fichier et sauvegarde les changements :

`autopep8 --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.py</span>

- Formate récursivement les fichiers dans un dossier et sauvegarde les changements :

`autopep8 --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>
