---
layout: page
title: linux/csplit (português (Brasil))
description: "Divide um arquivo em várias partes."
content_hash: 1b40460f6ab2e4cc3af05262b4fe3715d0e2835b
related_topics:
  - title: English version
    url: /en/linux/csplit.html
    icon: bi bi-globe
---
# csplit

Divide um arquivo em várias partes.
O padrão de nomenclatura dos arquivos será "xx00", "xx01" e assim por diante.
Mais informações: <https://www.gnu.org/software/coreutils/csplit>.

- Dividir um arquivo nas linhas 5 e 23:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">23</span>

- Dividir um arquivo a cada 5 linhas (este comando irá falhar se o total de linhas do arquivo não for divisível por 5):

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` {*}`

- Dividir um arquivo a cada 5 linhas, ignorando o fato do total de linhas ser divisível por 5:

`csplit -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` {*}`

- Dividir o arquivo na linha 5 e utilizar um prefixo específico para os arquivos de saída:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>

- Dividir um arquivo na linha que atenda a expressão regular:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressao_regular</span>`/`
