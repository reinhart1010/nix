---
layout: page
title: common/erl (italiano)
description: "Esegui e gestisci programmi nel linguaggio di programmazione Erlang."
content_hash: c6b9e9630049420a7b6a46daddcadeeef0dd7f79
related_topics:
  - title: English version
    url: /en/common/erl.html
    icon: bi bi-globe
---
# erl

Esegui e gestisci programmi nel linguaggio di programmazione Erlang.
Maggiori informazioni: <https://www.erlang.org>.

- Compila ed esegui un programma Erlang sequenziale come un comune script e poi esci:

`erlc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` && erl -noshell '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modulo:funzione(argomenti)</span>`, init:stop().'`

- Connetti ad un nodo Erlang in esecuzione:

`erl -remsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_nodo</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -sname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">soprannome</span>` -hidden -setcookie `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cookie_nodo_remoto</span>

- Fai caricare alla shell Erlang dei moduli da una directory:

`erl -pa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory_con_file_beam</span>
