---
layout: page
title: common/act (Nederlands)
description: "Voer GitHub-acties lokaal uit met behulp van Docker."
content_hash: 3a88f77f69e2c5d253b10447ae808769c8abe83e
last_modified_at: 2023-11-12
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

- Maak een lijst van de beschikbare acties:

`act -l`

- Voer de standaard evenement uit:

`act`

- Voer een specifiek evenement uit:

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">evenement_type</span>

- Voer een specifieke actie uit:

`act -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">actie_id</span>

- Voer de acties niet daadwerkelijk uit (d.w.z. een proefrit):

`act -n`

- Toon uitgebreide logboeken:

`act -v`

- Voer een specifieke workflow uit:

`act push -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/workflow</span>
