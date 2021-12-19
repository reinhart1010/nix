---
layout: page
title: common/tldr-lint (sh)
description: "Lintuje i formatira tldr stranice."
content_hash: 76e67507973bc68ad9b7e068b9bcc3bd0e4753f2
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
---
# tldr-lint

Lintuje i formatira tldr stranice.
Više informacija: <https://github.com/tldr-pages/tldr-lint>.

- Lintuj sve stranice:

`tldr-lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direktorijum_stranica</span>

- Formatiraj određenu stranicu u stdout:

`tldr-lint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stranica.md</span>

- Formatiraj sve stranice na njihovom mestu:

`tldr-lint --format --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direktorijum_stranica</span>
