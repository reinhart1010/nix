---
layout: page
title: windows/robocopy (Deutsch)
description: "Robustes Kopieren von Dateien und Ordnern."
content_hash: c1d58126fabc43f7aa97995d4aaf2a937e143623
related_topics:
  - title: English version
    url: /en/windows/robocopy.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># robocopy

Robustes Kopieren von Dateien und Ordnern.
Standardmäßig werden Dateien nur kopiert, wenn die Quell- und Zieldatei ein unterschiedliches Änderungsdatum oder eine unterschiedliche Dateigröße haben.
Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/robocopy>.

- Alle `.jpg` und `.bmp` Dateien aus dem einen Verzeichnis in ein anderes Verzeichnis kopieren:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/quelle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/ziel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.bmp</span>

- Alle Dateien und Unterverzeichnisse kopieren, einschließlich der leeren Verzeichnisse:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/quelle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/ziel</span>` /E`

- Ein Verzeichnis spiegeln/synchronisieren. Dabei wird Alles, was nicht in der Quelle vorhanden ist, gelöscht sowie alle Attribute und Berechtigungen übertragen:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/quelle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/ziel</span>` /MIR /COPYALL`

- Alle Dateien und Unterverzeichnisse kopieren, ausgenommen der Quelldateien, die älter sind als die vorhandenen Zieldateien:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/quelle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/ziel</span>` /E /XO`

- Gibt alle Dateien aus, die 50 MB und größer sind, anstatt sie zu kopieren:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/quelle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/ziel</span>` /MIN:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">52428800</span>` /L`

- Erlaubt das Fortsetzen des Vorgangs bei Netzwerkverlust, begrenzt die Anzahl an Versuchen auf 5 und die Wartezeit zwischen Versuchen auf 15 Sekunden:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/quelle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/ziel</span>` /Z /R:5 /W:15`

- Gibt detaillierte Nutzungshinweise aus:

`robocopy /?`
