---
layout: page
title: common/kitty (Deutsch)
description: "Ein schneller, funktionsreicher, auf der GPU basierender Terminal-Emulator."
content_hash: d7b6758e8259dc5ad747aac148e9971c9a1017a4
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/kitty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kitty

Ein schneller, funktionsreicher, auf der GPU basierender Terminal-Emulator.
Weitere Informationen: <https://sw.kovidgoyal.net/kitty/>.

- Öffne ein neues Terminal:

`kitty`

- Öffne ein Terminal mit einem festgelegten Titel für das Fenster:

`kitty --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Titel</span>`"`

- Starte die integrierte Farbschema-Auswahl:

`kitty +kitten themes`

- Zeige ein Bild im Terminal an:

`kitty +kitten icat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild</span>

- Kopiere den Inhalt von `stdin` in die Zwischenablage:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Beispiel</span>` | kitty +kitten clipboard`
