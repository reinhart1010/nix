---
layout: page
title: common/autoflake (français)
description: "Un outil pour enlever les imports et les variables inutilisés d'un code Python."
content_hash: 15bc5172130738695deeec4ce668bed6ce968e2c
related_topics:
  - title: English version
    url: /en/common/autoflake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autoflake.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/autoflake.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autoflake.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># autoflake

Un outil pour enlever les imports et les variables inutilisés d'un code Python.
Plus d'informations : <https://github.com/myint/autoflake>.

- Enlève les variables non-utilisées d'un fichier et affiche la différence :

`autoflake --remove-unused-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.py</span>

- Enlève les imports non-utilisés de plusieurs fichiers et affiche la différence :

`autoflake --remove-all-unused-imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier1.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier2.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier3.py</span>

- Enlève les variables non-utilisées d'un fichier, surcharge ce dernier :

`autoflake --remove-unused-variables --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.py</span>

- Enlève les variables non-utilisées de tous les fichiers d'un dossier de manière récursive, en les surchargeant :

`autoflake --remove-unused-variables --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>
