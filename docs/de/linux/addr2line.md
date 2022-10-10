---
layout: page
title: linux/addr2line (Deutsch)
description: "Konvertiere Adressen von Binärdateien in Dateinamen und Zeilennummern."
content_hash: 35585f286cc115dcf80a3c0f54a5e1ede530620d
related_topics:
  - title: English version
    url: /en/linux/addr2line.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/addr2line.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/addr2line.html
    icon: bi bi-globe
---
# addr2line

Konvertiere Adressen von Binärdateien in Dateinamen und Zeilennummern.
Weitere Informationen: <https://manned.org/addr2line>.

- Zeige den Dateinamen und die Zeilennummer des Quellcodes von einer Befehlsadresse einer ausführbaren Datei an:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/ausführbaren_datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse</span>

- Zeige den Funktionsnamen, Dateinamen und Zeilennummer an:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/executable</span>` --functions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse</span>

- Entmangele den Funktionsnamen für C++ Code:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/executable</span>` --functions --demangle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse</span>
