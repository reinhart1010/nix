---
layout: page
title: common/atrm (français)
description: "Supprime les travaux programmés par la commande `at` ou `batch`."
content_hash: e2db9b4ea8bcdab1ecbfd24e7638c546243624a3
related_topics:
  - title: English version
    url: /en/common/atrm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atrm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atrm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># atrm

Supprime les travaux programmés par la commande `at` ou `batch`.
Pour retrouver les numéros des travaux, utilise `atq`.
Plus d'informations : <https://manned.org/atrm>.

- Supprime le travail numéro 10 :

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Supprime plusieurs travaux, séparés par un espace :

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>
