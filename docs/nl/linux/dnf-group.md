---
layout: page
title: linux/dnf-group (Nederlands)
description: "Beheer virtuele collecties van pakketten op Fedora gebaseerde systemen."
content_hash: a2bea3e4ac9420505dddc6d0cd749eb11b5dde3a
last_modified_at: 2025-01-01
related_topics:
  - title: English version
    url: /en/linux/dnf-group.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf-group.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dnf-group.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dnf group

Beheer virtuele collecties van pakketten op Fedora gebaseerde systemen.
Meer informatie: <https://manned.org/man/dnf-group>.

- Maak een lijst van DNF-groepen, met geïnstalleerde en verwijderde status in een tabel:

`dnf group list`

- Toon DNF groepsinformatie, inclusief repository en optionele pakketten:

`dnf group info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groepsnaam</span>

- Installeer een DNF groep:

`dnf group install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groepsnaam</span>

- Verwijder een DNF groep:

`dnf group remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groepsnaam</span>

- Upgrade een DNF groep:

`dnf group upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groepsnaam</span>
