---
layout: page
title: osx/open (Deutsch)
description: "Öffne Dateien, Verzeichnisse und Anwendungen."
content_hash: 6170d51cd7727d30e7d234bbb6f226a5bc13b400
related_topics:
  - title: English version
    url: /en/osx/open.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/open.html
    icon: bi bi-globe
---
# open

Öffne Dateien, Verzeichnisse und Anwendungen.

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
