---
layout: page
title: osx/xcode-select (Deutsch)
description: "Wechsel zwischen verschiedenen Xcode Versionen und den enthaltenen Entwicklertools."
content_hash: 7c1127f332a00d2e7d1f310bfa63db63e46bf073
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/xcode-select.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xcode-select.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcode-select

Wechsel zwischen verschiedenen Xcode Versionen und den enthaltenen Entwicklertools.
Wird auch verwendet, um den Pfad zu Xcode zu aktualisieren, wenn dieser sich nach einer Installation geändert hat.
Weitere Informationen: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Installiere die Xcode Entwicklertools:

`xcode-select --install`

- Wähle einen bestimmten Pfad als aktives Entwicklerverzeichnis aus:

`sudo xcode-select --switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/Xcode.app/Contents/Developer</span>

- Wähle eine Xcode Version aus und ändere das aktive Entwicklerverzeichnis dahin:

`sudo xcode-select --switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/Xcode.app</span>

- Gib das derzeit aktive Entwicklerverzeichnis aus:

`xcode-select --print-path`

- Verwerfe alle vom Benutzer angegebenen Entwicklerverzeichnisse (fortan wird der Standardsuchmechanismus verwendet, um diese zu finden):

`sudo xcode-select --reset`
