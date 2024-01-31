---
layout: page
title: osx/route (português (Portugal))
description: "Alteração manual da tabela de rotas."
content_hash: ed6b625a59e59b4d9c39f59a834af8a4bee8f1de
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/route.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/route.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/route.html
    icon: bi bi-globe
tldri18n_status: 2
---
# route

Alteração manual da tabela de rotas.
Necessita de root.
Mais informações: <https://keith.github.io/xcode-man-pages/route.8.html>.

- Adiciona uma rota para um destino passando por um gateway:

`sudo route add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereco_ip_destino</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereco_gateway</span>`"`

- Adiciona uma rota para um rede /24 passando por um gateway:

`sudo route add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereco_ip_subnet</span>`/24" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereco_gateway</span>`"`

- Corre em modo de teste (não realiza alterações, apenas a mostra):

`sudo route -t add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereco_ip_destino</span>`/24" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereco_gateway</span>`"`

- Remove todas as rotas:

`sudo route flush`

- Remove uma rota especifica:

`sudo route delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereco_ip_destino</span>`/24"`

- Procura e mostra a rota para um destino (nome da máquina ou endereço IP):

`sudo route get "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>`"`
