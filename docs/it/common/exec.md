---
layout: page
title: common/exec (italiano)
description: "Sostituisci il processo corrente con un altro."
content_hash: c64aa28317eb6c7c07acff82095cfdebb4895eb6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/exec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exec

Sostituisci il processo corrente con un altro.
Maggiori informazioni: <https://linuxcommand.org/lc3_man_pages/exech.html>.

- Sostituisci con il comando specificato utilizzando le variabili di ambiente correnti:

`exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando -con -flag</span>

- Sostituisci con il comando specificato utilizzando un ambiente vuoto:

`exec -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando -con -flag</span>

- Sostituisci con il comando specificato ed esegui il login con la shell predefinita:

`exec -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando -con -flag</span>

- Sostituisci con il comando specificato e cambia il nome del processo:

`exec -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuovo_nome_processo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando -con -flag</span>
