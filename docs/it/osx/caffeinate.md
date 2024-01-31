---
layout: page
title: osx/caffeinate (italiano)
description: "Impedisci al mac di sospendersi."
content_hash: 79895af3f845e52d6b8fe841177dc7a6e7fb5ad0
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/osx/caffeinate.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/caffeinate.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/caffeinate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/caffeinate.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/caffeinate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/caffeinate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/caffeinate.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># caffeinate

Impedisci al mac di sospendersi.
Maggiori informazioni: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- Impedisci la sospensione per un'ora (3600 secondi):

`caffeinate -u -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Impedisci la sospensione fino al completamento dell'esecuzione di un comando:

`caffeinate -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Impedisci la sospensione fino alla pressione della combinazione di tasti Ctrl-C:

`caffeinate -i`
