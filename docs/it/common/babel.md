---
layout: page
title: common/babel (italiano)
description: "Un transpiler che converte codice JavaScript da sintassi ES6/ES7 ad ES5."
content_hash: 7a3e62a8a25329e4dcf1acbe98097ad08f9c3ea7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/babel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/babel.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/babel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/babel.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/babel.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/babel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# babel

Un transpiler che converte codice JavaScript da sintassi ES6/ES7 ad ES5.
Maggiori informazioni: <https://babeljs.io/>.

- Transpila uno specifico file e stampa il risultato su `stdout`:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Transpila un file e scrivi il risultato su uno specifico file di output:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_input</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_output</span>

- Transpila un file ogni volta che viene modificato:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>` --watch`

- Transpila un'intera directory di file:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_input</span>

- Transpila un'intera directory ignorando specifici file separati da virgola:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_input</span>` --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_ignorati</span>

- Transpila minimizzando il codice JavaScript in output:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_input</span>` --minified`

- Scegli un insieme di preset per formattare l'output:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_input</span>` --presets `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">preset</span>

- Mostra tutte le opzioni disponibili:

`babel --help`
