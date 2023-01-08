---
layout: page
title: linux/abroot (português (Brasil))
description: "O utilitário ABRoot fornece total imutabiliodade e atomicidade ao transacionar entre 2 estados da partição raíz (A⟺B)."
content_hash: e52d8f154554ebaaea74afd0d3ec8232ebc4d588
last_modified_at: 2023-01-08
related_topics:
  - title: English version
    url: /en/linux/abroot.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># abroot

O utilitário ABRoot fornece total imutabiliodade e atomicidade ao transacionar entre 2 estados da partição raíz (A⟺B).
Isso também permite transações sob demanda via um shell transacional.
Mais informações: <https://github.com/Vanilla-OS/ABRoot>.

- Saída do estado da partição raiz atual ou futuro:

`sudo abroot get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">present|future</span>

- Insira um shell transacional na futura partição raiz e alterne o root na próxima inicialização:

`sudo abroot shell`

- Executa um comando específico no shell transacional na partição raíz futura e troca para ela na próxima inicialização:

`sudo abroot exec "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Instala pacotes específicos no servidor dentro do shell transacional na partição raíz futura e troca para ela na próxima inicialização:

`sudo abroot exec apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote1 pacote2 ...</span>

- Atualiza a partição de inicialização (apenas para usuários avançados):

`sudo abroot _update-boot`

- Exibe ajuda:

`abroot --help`

- Exibe versão:

`abroot --version`
