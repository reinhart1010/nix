---
layout: page
title: common/arp (português (Brasil))
description: "Mostrar e manipular a cache ARP do sistema."
content_hash: 0cadd73a5b1f1c86fbaae68ec779d53e71af552e
related_topics:
  - title: English version
    url: /en/common/arp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/arp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/arp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp.html
    icon: bi bi-globe
---
# arp

Mostrar e manipular a cache ARP do sistema.
Mais informações: <https://manned.org/arp>.

- Mostrar a tabela arp atual:

`arp -a`

- Limpar toda a cache:

`sudo arp -a -d`

- Eliminar uma entrada específica:

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereço</span>

- Criar uma entrada:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereço</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereço_mac</span>
