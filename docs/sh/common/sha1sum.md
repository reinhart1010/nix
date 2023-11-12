---
layout: page
title: common/sha1sum (sh)
description: "Izračunava SHA1 kriptografske kontrolne brojeve."
content_hash: e7481577fe2d337494c001fd94c47b67dadc7974
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/sha1sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha1sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sha1sum

Izračunava SHA1 kriptografske kontrolne brojeve.
Više informacija: <https://www.gnu.org/software/coreutils/sha1sum>.

- Izračunaj SHA1 kontrolni broj za datoteku:

`sha1sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>

- Izračunaj SHA1 kontrolne brojeve za više datoteka:

`sha1sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka2</span>

- Pročitaj datoteku SHA1 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha1sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka.sha1</span>
