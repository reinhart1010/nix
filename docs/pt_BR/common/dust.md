---
layout: page
title: common/dust (português (Brasil))
description: "Dust oferece uma visão geral de quais diretórios estão usando espaço em disco."
content_hash: 31b42f29af7348d495a6a7ade0aea0d9c954d6d2
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/dust.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dust.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dust

Dust oferece uma visão geral de quais diretórios estão usando espaço em disco.
Mais informações: <https://github.com/bootandy/dust>.

- Exibe informações para o diretório atual:

`dust`

- Exibe informações para uma lista de diretórios separados por espaço:

`dust `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório1 caminho/para/diretório2 ...</span>

- Exibe 30 diretórios (o padrão é 21):

`dust --number-of-lines 30`

- Exibe informações para o diretório atual, com até 3 níveis de profundidade:

`dust --depth 3`

- Exibe os maiores diretórios no topo em ordem decrescente:

`dust --reverse`

- Ignora todos os arquivos e diretórios com um nome específico:

`dust --ignore-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_ou_nome_do_diretório</span>

- Não exibe barras de porcentagem e porcentagens:

`dust --no-percent-bars`
