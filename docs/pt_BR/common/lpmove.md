---
layout: page
title: common/lpmove (português (Brasil))
description: "Move a job or all jobs to another printer"
content_hash: 4dc5a41442453ef2a3161ac94410350c864129ff
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/lpmove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpmove

Move a job or all jobs to another printer
See also: `cancel`, `lp`, `lpr`, `lprm`.
More information: <https://openprinting.github.io/cups/doc/man-lpmove.html>.

- Move um trabalho específico para `nova_impressora`:

`lpmove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_trabalho</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_impressora</span>

- Move um trabalho de `antiga_impressora` para `nova_impressora`:

`lpmove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">antiga_impressora</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_trabalho</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_impressora</span>

- Move todos os trabalhos de `antiga_impressora` para `nova_impressora`:

`lpmove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">antiga_impressora</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_impressora</span>

- Move um trabalho específico para `nova_impressora` em um servidor específico:

`lpmove -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_trabalho</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_impressora</span>
