---
layout: page
title: common/atom (italiano)
description: "Un editor di testo cross-platform personalizzabile."
content_hash: 32a8aafa2c77e033d71acd68b2371328a6e8dbeb
last_modified_at: 2023-11-12
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># atom

Un editor di testo cross-platform personalizzabile.
I plugin sono gestiti da `apm`.
Maggiori informazioni: <https://atom.io/>.

- Apri un file o una directory:

`atom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Apri un file o una directory in una nuova finestra:

`atom -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Apri un file o una directory in una finestra esistente:

`atom --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Avvia Atom in safe mode (non carica nessun pacchetto):

`atom --safe`

- Impedisci ad Atom di creare un nuovo processo in background, lasciandolo in esecuzione nel terminale:

`atom --foreground`
