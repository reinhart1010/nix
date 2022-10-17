---
layout: page
title: windows/xcopy (Deutsch)
description: "Kopieren von Dateien und Verzeichnisbäumen."
content_hash: d9e972339397d88aa42d605ee5b55f155c6a5b4d
related_topics:
  - title: English version
    url: /en/windows/xcopy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/xcopy.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/xcopy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/xcopy.html
    icon: bi bi-globe
---
# xcopy

Kopieren von Dateien und Verzeichnisbäumen.
Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- Kopiere Datei(en) an den angegebenen Zielort:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ziel</span>

- Liste die zu kopierenden Dateien vor dem Kopieren auf:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ziel</span>` /p`

- Kopiere nur die Verzeichnisstruktur ohne Dateien:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ziel</span>` /t`

- Kopiere leere Verzeichnisse mit:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ziel</span>` /e`

- Behalte die Quell-Zugriffsrichtlinien (ACL) im Ziel Verzeichnis bei:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ziel</span>` /o`

- Setze den Vorgang nach Unterbrechung der Netzwerkverbindung fort:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ziel</span>` /z`

- Überschreibe bereits vorhandene Zieldateien automatisch:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ziel</span>` /y`

- Zeige die detaillierte Hilfe an:

`xcopy /?`
