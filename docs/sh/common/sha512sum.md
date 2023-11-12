---
layout: page
title: common/sha512sum (sh)
description: "Izračunava SHA512 kriptografske kontrolne brojeve."
content_hash: e0fca70d091d59ad5bc6e1b59214e8b7fc150178
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/sha512sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha512sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sha512sum

Izračunava SHA512 kriptografske kontrolne brojeve.
Više informacija: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Izračunaj SHA512 kontrolni broj za datoteku:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>

- Izračunaj SHA512 kontrolne brojeve za više datoteka:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka2</span>

- Pročitaj datoteku SHA512 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha512sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka.sha512</span>
