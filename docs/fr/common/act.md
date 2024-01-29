---
layout: page
title: common/act (français)
description: "Execute des GitHub Actions en local avec Docker."
content_hash: a1b4103cd934761f381af5dfdf91ac294c422406
last_modified_at: 2024-01-29
related_topics:
  - title: English version
    url: /en/common/act.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/act.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/act.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/act.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/act.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/act.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/act.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/act.html
    icon: bi bi-globe
tldri18n_status: 2
---
# act

Execute des GitHub Actions en local avec Docker.
Plus d'informations : <https://github.com/nektos/act>.

- [l]iste les jobs disponibles :

`act -l`

- Execute l'événement par défault :

`act`

- Execute un événement spécifique :

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type_d_événement</span>

- Execute un [j]ob spécifique :

`act -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_job</span>

- Ne pas lancer les actions maintenant (e.g un essai) :

`act -n`

- Affiche le journal en mode verbeux :

`act -v`

- Execute un [W]orkflow en particulier, avec l'événement push :

`act push -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/workflow</span>
