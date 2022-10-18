---
layout: page
title: common/atrm (polski)
description: "Usuwa zadania o zadanych identyfikatorach (numerach) wcześniej zakolejkowane przez `at` lub `batch`."
content_hash: 280fe886347e108e35d03944e562cd5368ac789c
related_topics:
  - title: English version
    url: /en/common/atrm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atrm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atrm.html
    icon: bi bi-globe
---
# atrm

Usuwa zadania o zadanych identyfikatorach (numerach) wcześniej zakolejkowane przez `at` lub `batch`.
Aby znaleźć numery zadań, użyj `atq`.
Więcej informacji: <https://manned.org/atrm>.

- Usuń zadanie numer 10:

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Usuń kilka zadań, oddzielonych spacjami:

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>
