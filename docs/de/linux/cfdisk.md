---
layout: page
title: linux/cfdisk (Deutsch)
description: "Ein Programm zur Verwaltung von Partitionstabellen mittels einer Curses-basierten UI."
content_hash: cc289d4952c08258efc28d6f1106d05638728ea1
related_topics:
  - title: English version
    url: /en/linux/cfdisk.html
    icon: bi bi-globe
---
# cfdisk

Ein Programm zur Verwaltung von Partitionstabellen mittels einer Curses-basierten UI.
Weitere Informationen: <https://manned.org/cfdisk>.

- Öffne das Partitionierungsinterface für eine bestimmte Festplatte:

`cfdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Erzeuge und bearbeite eine neue Partitionierungstabelle für eine bestimmte Festplatte:

`cfdisk --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
