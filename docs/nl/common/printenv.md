---
layout: page
title: common/printenv (Nederlands)
description: "Toon waarden van alle of specifieke omgevingsvariabelen."
content_hash: d299d66c77794c5d856e3c701f1a24902b395e3b
last_modified_at: 2024-06-26
related_topics:
  - title: English version
    url: /en/common/printenv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/printenv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># printenv

Toon waarden van alle of specifieke omgevingsvariabelen.
Meer informatie: <https://www.gnu.org/software/coreutils/printenv>.

- Toon key-value paren van alle omgevingsvariabelen:

`printenv`

- Toon de waarde van een specifieke variabele:

`printenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HOME</span>

- Toon de waarde van een variabele en eindig met NUL in plaats van een nieuwe regel:

`printenv --null `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HOME</span>
