---
layout: page
title: common/act (français)
description: "Execute des GitHub Actions en local avec Docker."
content_hash: bf5de94bab3d098f05e08b071683bfb9d3851637
related_topics:
  - title: English version
    url: /en/common/act.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/act.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/act.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/act.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># act

Execute des GitHub Actions en local avec Docker.
Plus d'informations : <https://github.com/nektos/act>.

- Liste les actions disponibles :

`act -l`

- Execute l'événement par défault :

`act`

- Execute un événement spécifique :

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type_d_événement</span>

- Execute une action spécifique :

`act -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_action</span>

- Ne pas lancer les actions maintenant (e.g un essai) :

`act -n`

- Affiche le journal en mode verbeux :

`act -v`
