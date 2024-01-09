---
layout: page
title: common/exec (italiano)
description: "Sostituisci il processo corrente con un altro."
content_hash: c8dc7f0cabd869f393f127edeba8cc497302d8bb
last_modified_at: 2024-01-09
related_topics:
  - title: English version
    url: /en/common/exec.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># exec

Sostituisci il processo corrente con un altro.
Maggiori informazioni: <https://manned.org/exec.1posix>.

- Sostituisci con il comando specificato utilizzando le variabili di ambiente correnti:

`exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando -con -flag</span>

- Sostituisci con il comando specificato utilizzando un ambiente vuoto:

`exec -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando -con -flag</span>

- Sostituisci con il comando specificato ed esegui il login con la shell predefinita:

`exec -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando -con -flag</span>

- Sostituisci con il comando specificato e cambia il nome del processo:

`exec -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuovo_nome_processo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando -con -flag</span>
