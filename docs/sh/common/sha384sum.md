---
layout: page
title: common/sha384sum (sh)
description: "Izračunava SHA384 kriptografske kontrolne brojeve."
content_hash: a8a1622e6a92f0203c14ea955e5a935cf6aec124
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/sha384sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha384sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sha384sum

Izračunava SHA384 kriptografske kontrolne brojeve.
Više informacija: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Izračunaj SHA384 kontrolni broj za datoteku:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>

- Izračunaj SHA384 kontrolne brojeve za više datoteka:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka2</span>

- Pročitaj datoteku SHA384 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha384sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka.sha384</span>
