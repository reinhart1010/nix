---
layout: page
title: common/sha256sum (sh)
description: "Izračunava SHA256 kriptografske kontrolne brojeve."
content_hash: df767047ee663d10ac9d905207bf5e9b6d607887
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/sha256sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha256sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sha256sum

Izračunava SHA256 kriptografske kontrolne brojeve.
Više informacija: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Izračunaj SHA256 kontrolni broj za datoteku:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>

- Izračunaj SHA256 kontrolne brojeve za više datoteka:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka2</span>

- Pročitaj datoteku SHA256 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha256sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka.sha256</span>
