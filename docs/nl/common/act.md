---
layout: page
title: common/act (Nederlands)
description: "Voer GitHub-acties lokaal uit met behulp van Docker."
content_hash: ee1ac0509c171e8e853d8d893e006f5506aaa2ce
last_modified_at: 2024-02-01
related_topics:
  - title: English version
    url: /en/common/act.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/act.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/act.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/act.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/act.html
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

Voer GitHub-acties lokaal uit met behulp van Docker.
Meer informatie: <https://github.com/nektos/act>.

- Maak een [l]ijst van de beschikbare acties:

`act -l`

- Voer de standaard evenement uit:

`act`

- Voer een specifiek evenement uit:

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">evenement_type</span>

- Voer een specifieke [j]ob uit:

`act -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Voer de acties [n]iet daadwerkelijk uit (d.w.z. een proefrit):

`act -n`

- Toon uitgebreide logboeken:

`act -v`

- Voer een specifieke [W]orkflow uit:

`act push -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/workflow</span>
