---
layout: page
title: common/envsubst (italiano)
description: "Sostituisci variabili di ambiente con il loro valore in stringhe di formato della shell."
content_hash: 0983f2ba8b521a2f8cf94d0f2e616c7f32abd483
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/envsubst.html
    icon: bi bi-globe
tldri18n_status: 2
---
# envsubst

Sostituisci variabili di ambiente con il loro valore in stringhe di formato della shell.
Le variabili da sostituire devono essere nella forma `${var}` oppure `$var`.
Maggiori informazioni: <https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html>.

- Sostituisci variabili di ambiente in `stdin` e stampa l'output su `stdout`:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$HOME</span>`' | envsubst`

- Sostituisci variabili di ambiente in un file input e stampa l'output su `stdout`:

`envsubst < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_input</span>

- Sostituisci variabili di ambiente in un file input e scrivi l'output su un file:

`envsubst < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_input</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_output</span>

- Sostituisci in un file input le variabili di ambiente specificate in una lista separata da spazi:

`envsubst '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$USER $HOME $SHELL</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_input</span>
