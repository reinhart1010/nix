---
layout: page
title: linux/ark (Deutsch)
description: "KDE-Archivierungstool."
content_hash: 1da2170be83e49bcaea0b46e7d09ea1b3c8d31b3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/ark.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ark

KDE-Archivierungstool.
Weitere Informationen: <https://docs.kde.org/stable5/en/ark/ark/>.

- Extrahiere ein Archiv ins aktuelle Verzeichnis:

`ark --batch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/archiv</span>

- Verändere das Verzeichnis in das extrahiert wird:

`ark --batch --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/archiv</span>

- Erstelle ein Archiv wenn es nicht existiert und füge Dateien hinzu:

`ark --add-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/archiv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1 pfad/zu/datei2 ...</span>
