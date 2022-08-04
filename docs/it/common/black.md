---
layout: page
title: common/black (italiano)
description: "Un formattatore automatico di codice Python."
content_hash: f736118c737764f107dd9e63f344e3aebf965083
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

- Auto-formatta un file o un'intera cartella:

`black `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_cartella</span>

- Formatta il codice che gli viene passato come stringa:

`black -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codice</span>`"`

- Mostra i cambiamenti che verrebbero applicati a ciascun file:

`black --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_cartella</span>

- Verifica se i file necessitano di auto-formattazione senza modificare nulla:

`black --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_cartella</span>

- Auto-formatta un file o una cartella senza produrre output:

`black --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_cartella</span>

- Auto-formatta un file o una cartella senza sostituire gli apici con le doppie virgolette:

`black --skip-string-normalization `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_cartella</span>
