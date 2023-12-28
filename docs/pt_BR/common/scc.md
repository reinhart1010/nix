---
layout: page
title: common/scc (português (Brasil))
description: "Utilitário escrito em GO que conta linhas de código."
content_hash: 208c4ebd8be3169af68276639e6deeb449c61ff3
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/scc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scc

Utilitário escrito em GO que conta linhas de código.
Mais informações: <https://github.com/boyter/scc>.

- Mostra o número de linhas de código no diretório atual:

`scc`

- Mostra o número de linhas de código de um diretório especificado:

`scc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Mostra o número de linhas de código por arquivo:

`scc --by-file`

- Mostra o resultado usando um formato específico (formato padrão é o `tabular`):

`scc --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tabular|wide|json|csv|cloc-yaml|html|html-table</span>

- Conta apenas os arquivos com as extensões especificadas:

`scc --include-ext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go, java, js</span>

- Exclui diretórios da contagem:

`scc --exclude-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.git,.hg</span>

- Mostra output organizado de acordo com o parâmetro especificado (organização padrão é `files`):

`scc --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">files|name|lines|blanks|code|comments|complexity</span>

- Mostra a tela de ajuda:

`scc -h`
