---
layout: page
title: common/tldr-lint (sh)
description: "Lintuje i formatira tldr stranice."
content_hash: 341bfecfbdf93c41e342c3de96e3e35be3a35511
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/tldr-lint.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tldr-lint.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr-lint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tldr-lint

Lintuje i formatira tldr stranice.
Više informacija: <https://github.com/tldr-pages/tldr-lint>.

- Lintuj sve stranice:

`tldr-lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direktorijum_stranica</span>

- Formatiraj određenu stranicu u `stdout`:

`tldr-lint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stranica.md</span>

- Formatiraj sve stranice na njihovom mestu:

`tldr-lint --format --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direktorijum_stranica</span>
