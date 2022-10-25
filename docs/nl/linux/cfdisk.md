---
layout: page
title: linux/cfdisk (Nederlands)
description: "Een programma voor het beheren van partitie tabellen en partities op een harde schijf met het gebruik van een UI."
content_hash: 69119db48edf93d4654bf363f9bc638d6668da5f
related_topics:
  - title: Deutsch version
    url: /de/linux/cfdisk.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/cfdisk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/cfdisk.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cfdisk

Een programma voor het beheren van partitie tabellen en partities op een harde schijf met het gebruik van een UI.
Meer informatie: <https://manned.org/cfdisk>.

- Start de partitie manipulator met een specifiek apparaat:

`cfdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Creëer een nieuwe partitie tabel voor een specifiek apparaat en beheer het:

`cfdisk --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
