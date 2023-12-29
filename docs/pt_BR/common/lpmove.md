---
layout: page
title: common/lpmove (português (Brasil))
description: "Move um ou todos os trabalhos para outra impressora."
content_hash: b83dc4d46dd510344292740f288d794f5d1c3114
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/lpmove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpmove

Move um ou todos os trabalhos para outra impressora.
Veja também: `cancel`, `lp`, `lpr`, `lprm`.
Mais informações: <https://openprinting.github.io/cups/doc/man-lpmove.html>.

- Move um trabalho específico para `nova_impressora`:

`lpmove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_trabalho</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_impressora</span>

- Move um trabalho de `antiga_impressora` para `nova_impressora`:

`lpmove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">antiga_impressora</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_trabalho</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_impressora</span>

- Move todos os trabalhos de `antiga_impressora` para `nova_impressora`:

`lpmove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">antiga_impressora</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_impressora</span>

- Move um trabalho específico para `nova_impressora` em um servidor específico:

`lpmove -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_trabalho</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nova_impressora</span>
