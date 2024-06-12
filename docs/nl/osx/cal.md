---
layout: page
title: osx/cal (Nederlands)
description: "Toon kalender informatie."
content_hash: b47836d12a6c4a55b962f6a8eae27b8022b76d80
last_modified_at: 2024-06-12
related_topics:
  - title: English version
    url: /en/osx/cal.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/cal.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/cal.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/cal.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/cal.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cal

Toon kalender informatie.
Meer informatie: <https://keith.github.io/xcode-man-pages/cal.1.html>.

- Toon een kalender voor de huidige maand:

`cal`

- Toon vorige, huidige en volgende maand:

`cal -3`

- Toon een kalender voor een specifieke maand (1-12 of de naam):

`cal -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maand</span>

- Toon een kalender voor het huidige jaar:

`cal -y`

- Toon een kalender voor een specifiek jaar (4 cijfers):

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jaar</span>

- Toon een kalender voor een specifieke maand en jaar:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jaar</span>

- Toon de datum van Pasen (Westerse Christelijke kerken) in een gegeven jaar:

`ncal -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jaar</span>
