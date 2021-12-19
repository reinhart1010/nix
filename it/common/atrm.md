---
layout: page
title: common/atrm (italiano)
description: "Rimuovi job programmati dai comandi `at` o `batch`."
content_hash: 40c368765b187784c5cb1e8299761cbd8375b12e
related_topics:
  - title: English version
    url: /en/common/atrm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atrm.html
    icon: bi bi-globe
---
# atrm

Rimuovi job programmati dai comandi `at` o `batch`.
Per trovare i numeri dei job utilizzare `atq`.
Maggiori informazioni: <https://man.archlinux.org/man/at.1>.

- Rimuovi il job numero 10:

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Rimuovi più job, separati da spazi:

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>
