---
layout: page
title: common/atom (italiano)
description: "Un editor di testo cross-platform personalizzabile."
content_hash: 89d6aa6caa934bf023d8c6de79a8c284748dbbfa
related_topics:
  - title: Deutsch version
    url: /de/common/atom.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/atom.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atom.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atom.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/atom.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atom.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/atom.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/atom.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># atom

Un editor di testo cross-platform personalizzabile.
I plugin sono gestiti da `apm`.
Maggiori informazioni: <https://atom.io/>.

- Apri un file o una cartella:

`atom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_cartella</span>

- Apri un file o una cartella in una nuova finestra:

`atom -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_cartella</span>

- Apri un file o una cartella in una finestra esistente:

`atom --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_cartella</span>

- Avvia Atom in safe mode (non carica nessun pacchetto):

`atom --safe`

- Impedisci ad Atom di creare un nuovo processo in background, lasciandolo in esecuzione nel terminale:

`atom --foreground`
