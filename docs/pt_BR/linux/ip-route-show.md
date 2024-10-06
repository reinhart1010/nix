---
layout: page
title: linux/ip-route-show (português (Brasil))
description: "Exibe subcomando para o gerenciamento de tabelas de roteamento de IP."
content_hash: ce3d849c47766d91670029b186896f5fbaf405ad
last_modified_at: 2024-10-06
related_topics:
  - title: English version
    url: /en/linux/ip-route-show.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip-route-show.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/ip-route-show.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip route show

Exibe subcomando para o gerenciamento de tabelas de roteamento de IP.
Mais informações: <https://manned.org/ip-route>.

- Exibe a tabela de roteamento:

`ip route show`

- Exibe a tabela de roteamento principal (mesmo que o primeiro exemplo):

`ip route show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main|254</span>

- Exibe a tabela de roteamento local:

`ip route show table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local|255</span>

- Exibe todas as tabelas de roteamento:

`ip route show table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all|unspec|0</span>

- Lista rotas apenas a partir de um dispositivo provido:

`ip route show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Lista rotas dentro de um escopo provido:

`ip route show scope link`

- Exibe o cache de roteamento:

`ip route show cache`

- Exibe apenas rotas IPv6 ou IPv4:

`ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-6|-4</span>` route show`
