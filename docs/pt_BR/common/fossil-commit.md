---
layout: page
title: common/fossil-commit (português (Brasil))
description: "Faz commit de arquivos para um repositório Fossil."
content_hash: 3186f0aa824e08757e1b35a9ec5afa40c0f8ba42
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/fossil-commit.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fossil-commit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fossil commit

Faz commit de arquivos para um repositório Fossil.
Mais informações: <https://fossil-scm.org/home/help/commit>.

- Cria uma nova versão contendo todas as alterações no checkout atual; o usuário será solicitado a inserir um comentário:

`fossil commit`

- Cria uma nova versão contendo todas as alterações no checkout atual, usando o comentário especificado:

`fossil commit --comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comentário</span>`"`

- Cria uma nova versão contendo todas as alterações no checkout atual com um comentário lido de um arquivo específico:

`fossil commit --message-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivos_de_mensagem_de_commit</span>

- Cria uma nova versão contendo alterações dos arquivos especificados; o usuário será solicitado a fornecer um comentário:

`fossil commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>
