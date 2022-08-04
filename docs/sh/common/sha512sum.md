---
layout: page
title: common/sha512sum (sh)
description: "Izračunava SHA512 kriptografske kontrolne brojeve."
content_hash: e0fca70d091d59ad5bc6e1b59214e8b7fc150178
related_topics:
  - title: English version
    url: /en/common/sha512sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha512sum.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sha512sum.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sha512sum

Izračunava SHA512 kriptografske kontrolne brojeve.
Više informacija: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Izračunaj SHA512 kontrolni broj za datoteku:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>

- Izračunaj SHA512 kontrolne brojeve za više datoteka:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka2</span>

- Pročitaj datoteku SHA512 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha512sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka.sha512</span>
