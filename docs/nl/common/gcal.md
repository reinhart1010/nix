---
layout: page
title: common/gcal (Nederlands)
description: "Toon een kalender."
content_hash: dc179d8f7acec595518b38e685329090d9c4e0a6
last_modified_at: 2024-06-12
related_topics:
  - title: English version
    url: /en/common/gcal.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gcal.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcal.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcal

Toon een kalender.
More information: <https://www.gnu.org/software/gcal>.

- Toon een kalender voor de huidige maand:

`gcal`

- Toon de kalender voor de maand februari van het jaar 2010:

`gcal 2 2010`

- Toon een kalender met weeknummers:

`gcal --with-week-number`

- Verander de startdag van de week naar de eerste dag van de week (maandag):

`gcal --starting-day=1`

- Toon de vorige, huidige en volgende maand rondom vandaag:

`gcal .`
