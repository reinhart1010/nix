---
layout: page
title: common/scc (português (Brasil))
description: "Utilitário escrito em GO que conta linhas de código."
content_hash: 8ddbaf9fb3b28eba24bd55c8f236d13a35ba679c
related_topics:
  - title: English version
    url: /en/common/scc.html
    icon: bi bi-globe
---
# scc

Utilitário escrito em GO que conta linhas de código.
Mais informações: <https://github.com/boyter/scc>.

- Mostrar o número de linhas de código no diretório atual:

`scc`

- Mostrar o número de linhas de código de um diretório especificado:

`scc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Mostrar o número de linhas de código por arquivo:

`scc --by-file`

- Mostrar o resultado usando um formato específico (formato padrão é o `tabular`):

`scc --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tabular|wide|json|csv|cloc-yaml|html|html-table</span>

- Contar apenas os arquivos com as extensões especificadas:

`scc --include-ext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go, java, js</span>

- Excluir diretórios da contagem:

`scc --exclude-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.git,.hg</span>

- Mostrar output organizado de acordo com o parâmetro especificado (organização padrão é `files`):

`scc --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">files|name|lines|blanks|code|comments|complexity</span>

- Mostra a tela de ajuda:

`scc -h`
