---
layout: page
title: common/df (italiano)
description: "Fornisce una panoramica dello spazio utilizzato dai file system sui dischi."
content_hash: a2225b8295dacebd2e10a73a45b1180bb2789ce4
related_topics:
  - title: Deutsch version
    url: /de/common/df.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/df.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/df.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/df.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># df

Fornisce una panoramica dello spazio utilizzato dai file system sui dischi.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/df>.

- Mostra tutti i file system ed il loro utilizzo del disco:

`df`

- Mostra tutti i file system ed il loro utilizzo del disco in formato leggibile dall'uomo:

`df -h`

- Mostra il file system ed contenente il file o directory dato ed il suo utilizzo del disco:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_directory</span>
