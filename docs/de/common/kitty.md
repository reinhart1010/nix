---
layout: page
title: common/kitty (Deutsch)
description: "Ein schneller, funktionsreicher, auf der GPU basierender Terminal-Emulator."
content_hash: 9e0550460a07c5a3d06462f68deee9c0ab860199
last_modified_at: 2023-10-22
related_topics:
  - title: English version
    url: /en/common/kitty.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kitty

Ein schneller, funktionsreicher, auf der GPU basierender Terminal-Emulator.
Weitere Informationen: <https://sw.kovidgoyal.net/kitty/>.

- Öffne ein neues Terminal:

`kitty`

- Öffne ein Terminal mit einem festgelegten Titel für das Fenster:

`kitty --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Titel</span>`"`

- Starte die integrierte Farbschema-Auswahl:

`kitty +kitten themes`

- Zeige ein Bild im Terminal an:

`kitty +kitten icat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/bild</span>

- Kopiere den Inhalt von `stdin` in die Zwischenablage:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Beispiel</span>` | kitty +kitten clipboard`
