---
layout: page
title: linux/csplit (português (Brasil))
description: "Divide um arquivo em várias partes."
content_hash: c8b33ddab5cfc960daca0c91ef9f91404967f0a5
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/csplit.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/csplit.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/csplit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csplit

Divide um arquivo em várias partes.
O padrão de nomenclatura dos arquivos será "xx00", "xx01" e assim por diante.
Mais informações: <https://www.gnu.org/software/coreutils/manual/html_node/csplit-invocation.html>.

- Divide um arquivo nas linhas 5 e 23:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` 5 23`

- Divide um arquivo a cada 5 linhas (este comando irá falhar se o total de linhas do arquivo não for divisível por 5):

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` 5 {*}`

- Divide um arquivo a cada 5 linhas, ignorando o fato do total de linhas ser divisível por 5:

`csplit -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` 5 {*}`

- Divide o arquivo na linha 5 e utiliza um prefixo específico para os arquivos de saída:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` 5 -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>

- Divide um arquivo na linha que atenda a expressão regular:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressao_regular</span>`/`
