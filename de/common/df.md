---
layout: page
title: common/df (Deutsch)
description: "Verschafft einen Überblick über verfügbaren Speicherplatz im Dateisystem."
content_hash: 4f6c322f2efee46b26539eac713dc5b67f842d3d
related_topics:
  - title: English version
    url: /en/common/df.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/df.html
    icon: bi bi-globe
---
# df

Verschafft einen Überblick über verfügbaren Speicherplatz im Dateisystem.
Weitere Informationen: <https://www.gnu.org/software/coreutils/df>.

- Zeige verfügbaren Platz auf allen eingehängten Dateisystemen:

`df`

- Zeige verfügbaren Platz auf allen eingehängten Dateisystemen in einem menschenlesbaren Format:

`df -h`

- Zeige das Dateisystem und dessen Speicherverbrauch, das die angegebene Datei oder Verzeichnis enthält:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>

- Zeige Statistiken über die Anzahl freier Inodes:

`df -i`

- Zeige alle Dateisysteme bis auf die eines bestimmten Typs:

`df -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>
