---
layout: page
title: linux/ip (português (Brasil))
description: "Mostra / manipula roteamento, dispositivos, roteamento baseado em póliticas e túneis."
content_hash: 8b02ab3a1d8f7335bb582bee2493590c5c6a970a
last_modified_at: 2024-10-05
related_topics:
  - title: Deutsch version
    url: /de/linux/ip.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/ip.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip

Mostra / manipula roteamento, dispositivos, roteamento baseado em póliticas e túneis.
Alguns subcomandos como `address` têm suas pŕoprias documentações de uso.
Mais informações: <https://www.manned.org/ip.8>.

- Lista interfaces com informações detalhadas:

`ip address`

- Lista interfaces com breves informações sobre a camada de rede:

`ip -brief address`

- Lista interfaces com breves informações sobre a camada de link de dados:

`ip -brief link`

- Exibe a tabela de roteamento:

`ip route`

- Mostra vizinhos (ARP tabela):

`ip neighbour`

- Ativa / desativa uma interface:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">up|down</span>

- Adiciona / remove um endereço de IP a uma interface:

`ip addr add/del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Adiciona uma rota padrão:

`ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
