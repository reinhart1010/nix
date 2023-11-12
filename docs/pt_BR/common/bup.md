---
layout: page
title: common/bup (português (Brasil))
description: "Sistema de backup baseado no formato Git packfile, oferecendo salvamentos incrementais e desduplicação global."
content_hash: 7a4eb9cc3e97422102549821f60b321f749c6aaa
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bup.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bup.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bup

Sistema de backup baseado no formato Git packfile, oferecendo salvamentos incrementais e desduplicação global.
Mais informações: <https://github.com/bup/bup>.

- Inicializa um repositório de backup no diretório local especificado:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/repositório</span>` init`

- Prepara um determinado diretório antes de fazer um backup:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/repositório</span>` index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Faz o backup de um diretório para o repositório:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/repositório</span>` save -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_backup</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Exibe os snapshots de backup armazenados atualmente no repositório:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/repositório</span>` ls`

- Restaura um snapshot de backup específico para um diretório de destino:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/repositório</span>` restore -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_de_destino</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_backup</span>
