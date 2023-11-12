---
layout: page
title: common/sha224sum (sh)
description: "Izračunava SHA224 kriptografske kontrolne brojeve."
content_hash: 3460c15824203cf786ba0b2845346290482ee49d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/sha224sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha224sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sha224sum

Izračunava SHA224 kriptografske kontrolne brojeve.
Više informacija: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Izračunaj SHA224 kontrolni broj za datoteku:

`sha224sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>

- Izračunaj SHA224 kontrolne brojeve za više datoteka:

`sha224sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka2</span>

- Pročitaj datoteku SHA224 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha224sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka.sha224</span>
