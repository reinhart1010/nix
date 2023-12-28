---
layout: page
title: linux/csplit (português (Brasil))
description: "Divide um arquivo em várias partes."
content_hash: 149a89692cdacdfa298b43f327c80e4f71820b26
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/csplit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csplit

Divide um arquivo em várias partes.
O padrão de nomenclatura dos arquivos será "xx00", "xx01" e assim por diante.
Mais informações: <https://www.gnu.org/software/coreutils/csplit>.

- Divide um arquivo nas linhas 5 e 23:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">23</span>

- Divide um arquivo a cada 5 linhas (este comando irá falhar se o total de linhas do arquivo não for divisível por 5):

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` {*}`

- Divide um arquivo a cada 5 linhas, ignorando o fato do total de linhas ser divisível por 5:

`csplit -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` {*}`

- Divide o arquivo na linha 5 e utiliza um prefixo específico para os arquivos de saída:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>

- Divide um arquivo na linha que atenda a expressão regular:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressao_regular</span>`/`
