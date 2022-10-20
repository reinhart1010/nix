---
layout: page
title: common/black (italiano)
description: "Un formattatore automatico di codice Python."
content_hash: fed25ff1a99ebfe9e71da130ffc944ec68a66a52
related_topics:
  - title: English version
    url: /en/common/black.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/black.html
    icon: bi bi-globe
---
# black

Un formattatore automatico di codice Python.
Maggiori informazioni: <https://github.com/psf/black>.

- Auto-formatta un file o un'intera directory:

`black `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Formatta il codice che gli viene passato come stringa:

`black -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codice</span>`"`

- Mostra i cambiamenti che verrebbero applicati a ciascun file:

`black --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Verifica se i file necessitano di auto-formattazione senza modificare nulla:

`black --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Auto-formatta un file o una directory senza produrre output:

`black --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Auto-formatta un file o una directory senza sostituire gli apici con le doppie virgolette:

`black --skip-string-normalization `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>
