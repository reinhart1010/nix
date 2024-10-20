---
layout: page
title: common/gh-codespace (português (Brasil))
description: "Conecta e gerencia seus codespaces no GitHub."
content_hash: 7e1cd20a340e188dd5d608e8c615fa8e57c2510c
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gh-codespace.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gh-codespace.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/gh-codespace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh codespace

Conecta e gerencia seus codespaces no GitHub.
Mais informações: <https://cli.github.com/manual/gh_codespace>.

- Cria um codespace no GitHub interativamente:

`gh codespace create`

- Lista todos os codespaces disponíveis:

`gh codespace list`

- Conecta a um codespace via SSH interativamente:

`gh codespace ssh`

- Transfere um arquivo específico para um codespace interativamente:

`gh codespace cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_fonte</span>` remote:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_remoto</span>

- Lista os ports de um codespace interativamente:

`gh codespace ports`

- Exibe os registros de um codespace interativamente:

`gh codespace logs`

- Exclui um codespace interativamente:

`gh codespace delete`

- Exibe ajuda para um subcomando:

`gh codespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code|cp|create|delete|edit|...</span>` --help`
