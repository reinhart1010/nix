---
layout: page
title: common/man (italiano)
description: "Formatta e mostra pagine manuale."
content_hash: f39fb0080a1d102f342a267407394733a5f464b4
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/man.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/man.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/man.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/man.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/man.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/man.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># man

Formatta e mostra pagine manuale.
Maggiori informazioni: <https://manned.org/man>.

- Mostra la pagina di manuale di un comando:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Mostra la pagina di manuale per un comando dalla sezione 7:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Mostra il percorso in cui vengono cercate le pagine:

`man --path`

- Mostra la posizione di una pagina invece che la pagina stessa:

`man -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Cerca pagine di manuale che contengano una certa stringa:

`man -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ricerca</span>
