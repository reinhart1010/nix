---
layout: page
title: osx/emond (português (Brasil))
description: "Serviço Event Monitor que aceita eventos de vários serviços, os executa por meio de um mecanismo de regras simples, e executa ações."
content_hash: e0e8ec3e17e3fcfc56b626d1e2cb87e3f9d16421
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/emond.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/emond.html
    icon: bi bi-globe
tldri18n_status: 2
---
# emond

Serviço Event Monitor que aceita eventos de vários serviços, os executa por meio de um mecanismo de regras simples, e executa ações.
As ações podem executar comandos, enviar e-mails, ou mensagens SMS.
Mais informações: <https://keith.github.io/xcode-man-pages/emond.8.html>.

- Inicia o daemon:

`emond`

- Especifica as regras para o emond processar, fornecendo um caminho para um arquivo ou diretório:

`emond -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Usa um arquivo de configuração específico:

`emond -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/configuração</span>
