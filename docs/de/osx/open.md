---
layout: page
title: osx/open (Deutsch)
description: "Öffne Dateien, Verzeichnisse und Anwendungen."
content_hash: 0d1be3c0de25e24d917121f239c0a850255219a9
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/open.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/open.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/open.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/open.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># open

Öffne Dateien, Verzeichnisse und Anwendungen.
Weitere Informationen: <https://keith.github.io/xcode-man-pages/open.1.html>.

- Öffne eine Datei in der zugehörigen Anwendung:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Führe eine grafische macOS-Anwendung aus:

`open -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anwendung</span>

- Führe eine grafische macOS-Anwendung basierend auf der Bundle-Kennung aus (siehe `osascript` für eine einfache Möglichkeit, diese zu identifizieren):

`open -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.domain.anwendung</span>

- Öffne das aktuelle Verzeichnis im Finder:

`open .`

- Zeige eine Datei im Finder an:

`open -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Öffne alle Dateien einer bestimmten Erweiterung im aktuellen Verzeichnis mit der zugehörigen Anwendung:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>
