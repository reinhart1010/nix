---
layout: page
title: linux/apt-file (italiano)
description: "Cerca un file dentro un pacchetto APT, includendo quelli non ancora installati."
content_hash: f0d7d513fcc03fd2c0b5d6b4d7dc9fe0443cba57
last_modified_at: 2024-03-14
related_topics:
  - title: català version
    url: /ca/linux/apt-file.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-file.html
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
  - title: Indonesia version
    url: /id/linux/apt-file.html
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apt-file

Cerca un file dentro un pacchetto APT, includendo quelli non ancora installati.
Maggiori informazioni: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Aggiorna il database dei metadati:

`sudo apt update`

- Cerca i pacchetti che contengono un file o un percorso specificato:

`apt-file search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parte/del/filename</span>

- Elenca i contenuti di un pacchetto specifico:

`apt-file list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_pacchetto</span>
