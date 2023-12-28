---
layout: page
title: osx/xcode-select (Deutsch)
description: "Wechsel zwischen verschiedenen Xcode Versionen und den enthaltenen Entwicklertools."
content_hash: aefb3fc1bd269e91df21c01cdb215b45502a3e23
last_modified_at: 2023-12-28
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

`xcode-select --switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/Xcode.app/Contents/Developer</span>

- Wähle eine Xcode Version aus und ändere das aktive Entwicklerverzeichnis dahin:

`xcode-select --switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/Xcode.app</span>

- Gib das derzeit aktive Entwicklerverzeichnis aus:

`xcode-select --print-path`

- Verwerfe alle vom Benutzer angegebenen Entwicklerverzeichnisse (fortan wird der Standardsuchmechanismus verwendet, um diese zu finden):

`sudo xcode-select --reset`
