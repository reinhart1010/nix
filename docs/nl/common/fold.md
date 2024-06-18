---
layout: page
title: common/fold (Nederlands)
description: "Breek elke regel in een invoerbestand af om in een gespecificeerde breedte te passen en toon het in `stdout`."
content_hash: cd88c02e37a37c69b4e8806974415e61acdb9b1a
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/common/fold.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fold.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fold

Breek elke regel in een invoerbestand af om in een gespecificeerde breedte te passen en toon het in `stdout`.
Meer informatie: <https://manned.org/fold.1p>.

- Breek elke regel af op de standaard breedte (80 tekens):

`fold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Breek elke regel af op een breedte van "30":

`fold -w30 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Breek elke regel af op een breedte van "5" en breek de regel bij spaties (zet elk door spaties gescheiden woord op een nieuwe regel, woorden langer dan 5 tekens worden afgebroken):

`fold -w5 -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
