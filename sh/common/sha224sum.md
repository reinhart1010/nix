---
layout: page
title: common/sha224sum (sh)
description: "Izračunava SHA224 kriptografske kontrolne brojeve."
content_hash: 3460c15824203cf786ba0b2845346290482ee49d
related_topics:
  - title: English version
    url: /en/common/sha224sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha224sum.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sha224sum.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sha224sum

Izračunava SHA224 kriptografske kontrolne brojeve.
Više informacija: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Izračunaj SHA224 kontrolni broj za datoteku:

`sha224sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>

- Izračunaj SHA224 kontrolne brojeve za više datoteka:

`sha224sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka2</span>

- Pročitaj datoteku SHA224 brojeva i proveri da li se svi kontrolni brojevi datoteka poklapaju:

`sha224sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka.sha224</span>
