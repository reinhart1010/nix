---
layout: page
title: linux/addr2line (Deutsch)
description: "Konvertiere Adressen von Binärdateien in Dateinamen und Zeilennummern."
content_hash: 386d3c38581545c145d3fc1324f54d7b5c562b82
related_topics:
  - title: English version
    url: /en/linux/addr2line.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/addr2line.html
    icon: bi bi-globe
---
# addr2line

Konvertiere Adressen von Binärdateien in Dateinamen und Zeilennummern.
Weitere Informationen: <https://manned.org/addr2line>.

- Zeige den Dateinamen und die Zeilennummer des Quellcodes von einer Befehlssadresse einer ausführbaren Datei an:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/ausführbaren_datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse</span>

- Zeige den Funktionsnamen, Dateinamen und Zeilennummer an:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/executable</span>` --functions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse</span>

- Entmangele den Funktionsnamen für C++ Code:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/executable</span>` --functions --demangle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse</span>
