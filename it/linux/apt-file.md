---
layout: page
title: linux/apt-file (italiano)
description: "Cerca un file dentro un pacchetto apt, includendo quelli non ancora installati."
content_hash: 2f874529384cbe3b5bb74869e1ffdf3debaef4c8
related_topics:
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
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-file.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-file.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apt-file.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apt-file

Cerca un file dentro un pacchetto apt, includendo quelli non ancora installati.
Maggiori informazioni: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Aggiorna il database dei metadati:

`sudo apt update`

- Cerca i pacchetti che contengono un file o un percorso specificato:

`apt-file search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parte/del/filename</span>

- Elenca i contenuti di un pacchetto specifico:

`apt-file list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_pacchetto</span>
