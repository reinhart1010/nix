---
layout: page
title: osx/emond (português (Brasil))
description: "Serviço Event Monitor que aceita eventos de vários serviços, os executa por meio de um mecanismo de regras simples, e executa ações."
content_hash: 701f25e0b1c674c53c2a5d6d58eb78ccc3d6c332
related_topics:
  - title: English version
    url: /en/osx/emond.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># emond

Serviço Event Monitor que aceita eventos de vários serviços, os executa por meio de um mecanismo de regras simples, e executa ações.
As ações podem executar comandos, enviar e-mails, ou mensagens SMS.
Mais informações: <https://www.manpagez.com/man/8/emond/>.

- Inicia o daemon:

`emond`

- Especifica as regras para o emond processar, fornecendo um caminho para um arquivo ou diretório:

`emond -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Usa um arquivo de configuração específico:

`emond -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/configuração</span>
