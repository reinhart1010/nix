---
layout: page
title: linux/apt-file (Deutsch)
description: "Suche nach Dateien in apt-Paketen, auch in den nicht-installierten."
content_hash: 44a9bc164f54f8ebde7cc4b3bda859a56bc3f325
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/apt-file.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-file.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-file.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-file.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-file.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-file.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-file.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-file

Suche nach Dateien in apt-Paketen, auch in den nicht-installierten.
Weitere Informationen: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Aktualisiere die Metadatenbank:

`sudo apt update`

- Suche nach Paketen, die die/den spezifizierten Pfad/Datei enthalten:

`apt-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search|find</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/datei</span>

- Liste die Inhalte eines bestimmten Pakets auf:

`apt-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show|list</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Suche nach Paketen auf die die Regular Expression zutrifft:

`apt-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search|find</span>` --regexp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>
