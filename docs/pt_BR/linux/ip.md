---
layout: page
title: linux/ip (português (Brasil))
description: "Mostra / manipula roteamento, dispositivos, roteamento baseado em póliticas e túneis."
content_hash: f1dab089ae92972a9f57b4af3a50c43da0c43c74
last_modified_at: 2022-12-29
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
  - title: Türkçe version
    url: /tr/linux/ip.html
    icon: bi bi-globe
---
# ip

Mostra / manipula roteamento, dispositivos, roteamento baseado em póliticas e túneis.
Alguns subcomandos como `ip address` têm suas pŕoprias documentações de uso.
Mais informações: <https://www.man7.org/linux/man-pages/man8/ip.8.html>.

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

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` up/down`

- Adiciona / remove um endereço de IP a uma interface:

`ip addr add/del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Adiciona uma rota padrão:

`ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
