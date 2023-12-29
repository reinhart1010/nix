---
layout: page
title: common/black (italiano)
description: "Un formattatore automatico di codice Python."
content_hash: d2de7eafe92b7cef67d129ade746d6a9f140fea0
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/black.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/black.html
    icon: bi bi-globe
tldri18n_status: 2
---
# black

Un formattatore automatico di codice Python.
Maggiori informazioni: <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html>.

- Auto-formatta un file o un'intera directory:

`black `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Formatta il codice che gli viene passato come stringa:

`black -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codice</span>`"`

- Verifica se i file necessitano di auto-formattazione senza modificare nulla:

`black --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Mostra i cambiamenti che verrebbero applicati a ciascun file:

`black --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Auto-formatta un file o una directory senza produrre output:

`black --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Auto-formatta un file o una directory senza sostituire gli apici con le doppie virgolette:

`black --skip-string-normalization `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>
