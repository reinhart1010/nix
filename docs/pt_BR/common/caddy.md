---
layout: page
title: common/caddy (português (Brasil))
description: "Um servidor web open source, pronto para empresas, com HTTPS automático, escrito em Go."
content_hash: 4b4ee7498b38a8e44f6276ccdf6d6315c5939de8
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/caddy.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/caddy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# caddy

Um servidor web open source, pronto para empresas, com HTTPS automático, escrito em Go.
Mais informações: <https://caddyserver.com>.

- Inicia Caddy em primeiro plano:

`caddy run`

- Inicia Caddy com um arquivo Caddy específico:

`caddy run --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivoCaddy</span>

- Inicia Caddy no plano de fundo:

`caddy start`

- Para um processo Caddy em plano de fundo:

`caddy stop`

- Executa um servidor de arquivo simples na porta especificada, com uma interface navegável:

`caddy file-server --listen :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>` --browse`

- Executa um servidor proxy reverso:

`caddy reverse-proxy --from :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --to localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>
