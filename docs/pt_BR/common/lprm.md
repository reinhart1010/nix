---
layout: page
title: common/lprm (português (Brasil))
description: "Cancela trabalhos de impressão na fila de um servidor."
content_hash: 9520db4d8438ed47b23b8cd978561ff899fe90b2
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/lprm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lprm

Cancela trabalhos de impressão na fila de um servidor.
Veja também: `lpq`.
Mais informações: <https://openprinting.github.io/cups/doc/man-lprm.html>.

- Cancela o trabalho atual na impressora padrão:

`lprm`

- Cancela um trabalho de um servidor específico:

`lprm -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor[:porta]</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_trabalho</span>

- Cancela múltiplos trabalhos com uma conexão criptografada com o servidor:

`lprm -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_trabalho1 id_do_trabalho2 ...</span>

- Cancela todos os trabalhos:

`lprm -`

- Cancela o trabalho atual de uma impressora ou classe específica:

`lprm -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino[/instância]</span>
