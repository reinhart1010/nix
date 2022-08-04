---
layout: page
title: linux/dmesg (português (Brasil))
description: "Escreve as mensagens do kernel na terminal."
content_hash: ad56bcbe3d859c567d7ccdccb26dc55c2f30d897
related_topics:
  - title: English version
    url: /en/linux/dmesg.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dmesg.html
    icon: bi bi-globe
---
# dmesg

Escreve as mensagens do kernel na terminal.
Mais informações: <https://manned.org/dmesg>.

- Exibir as mensagens do kernel:

`dmesg`

- Exibir as mensagens de erro do kernel:

`dmesg --level err`

- Exibir as mensagens do kernel e manter o terminal esperando por novas menagens, semelhante ao `tail -f` (disponível nas versões 3.5.0 e superiores do kernel):

`dmesg -w`

- Exibir a quantidade de memória física disponível no sistema:

`dmesg | grep -i memory`

- Exibir as mensagens do kernel divididas em páginas:

`dmesg | less`

- Exibir as menagens do kernel com data/hora (disponível nas versões 3.5.0 e superiores do kernel):

`dmesg -T`

- Exibir as mensagens do kernel em um formato de fácil leitura (disponível nas versões 3.5.0 e superiores do kernel):

`dmesg -H`

- Exibir as mensagens do kernel utilizando cores (disponível nas versões 3.5.0 e superiores do kernel):

`dmesg -L`
