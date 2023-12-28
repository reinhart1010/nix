---
layout: page
title: common/cancel (português (Brasil))
description: "Cancela trabalhos de impressão."
content_hash: 68417128cf0afb9b5ed725d348d2460b70e2a65e
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/cancel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cancel

Cancela trabalhos de impressão.
Veja também: `lp`, `lpmove`, `lpstat`.
Mais informações: <https://openprinting.github.io/cups/doc/man-cancel.html>.

- Cancela o trabalho atual da impressora padrão (definida com `lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">impressora</span>):

`cancel`

- Cancela todos os trabalhos da impressora padrão que pertencem a um usuário específico:

`cancel -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>

- Cancela o trabalho atual de uma impressora específica:

`cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">impressora</span>

- Cancela um trabalho específico de uma impressora específica:

`cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">impressora</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_trabalho</span>

- Cancela todos os trabalhos de todas as impressoras:

`cancel -a`

- Cancela todos os trabalhos de uma impressora específica:

`cancel -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">impressora</span>

- Cancela o trabalho atual de um servidor específico e então deleta os arquivos de dados do trabalho:

`cancel -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>` -x`
