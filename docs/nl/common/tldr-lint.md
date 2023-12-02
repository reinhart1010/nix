---
layout: page
title: common/tldr-lint (Nederlands)
description: "Controleert en formatteert `tldr` pagina's."
content_hash: e0c3c89ad33029d72c3557816506b67b8e18963c
last_modified_at: 2023-12-02
related_topics:
  - title: English version
    url: /en/common/tldr-lint.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tldr-lint.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr-lint.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr-lint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tldr-lint

Controleert en formatteert `tldr` pagina's.
Meer informatie: <https://github.com/tldr-pages/tldr-lint>.

- Controleer alle pagina's:

`tldr-lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">map_met_paginas</span>

- Formatteer een specifieke pagina naar `stdout`:

`tldr-lint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pagina.md</span>

- Formateer alle pagina's ter plaatse:

`tldr-lint --format --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">map_met_paginas</span>
