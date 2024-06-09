---
layout: page
title: osx/date (Nederlands)
description: "Stel de systeemdatum in of toon deze."
content_hash: 2c8b4be368d0c4b0c63297c4e06cf51c261c5d7f
last_modified_at: 2024-06-09
related_topics:
  - title: English version
    url: /en/osx/date.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/date.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/osx/date.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/date.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/date.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/date.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/date.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># date

Stel de systeemdatum in of toon deze.
Meer informatie: <https://keith.github.io/xcode-man-pages/date.1.html>.

- Toon de huidige datum in het standaardformaat van de locale:

`date +%c`

- Toon de huidige datum in UTC en ISO 8601-formaat:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- Toon de huidige datum als een Unix timestamp (seconden sinds de Unix-epoch):

`date +%s`

- Toon een specifieke datum (gerepresenteerd als een Unix timestamp) met het standaard formaat:

`date -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1473305798</span>
