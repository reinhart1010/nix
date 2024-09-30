---
layout: page
title: linux/dmesg (português (Brasil))
description: "Escreve as mensagens do kernel na terminal."
content_hash: 13b80bffabd13a855fadf929f0858437cdf54a1e
last_modified_at: 2024-09-30
related_topics:
  - title: català version
    url: /ca/linux/dmesg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dmesg.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dmesg.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

Escreve as mensagens do kernel na terminal.
Mais informações: <https://manned.org/dmesg>.

- Exibe as mensagens do kernel:

`sudo dmesg`

- Exibe as mensagens de erro do kernel:

`sudo dmesg --level err`

- Exibe as mensagens do kernel e manter o terminal esperando por novas menagens, semelhante ao `tail -f` (disponível nas versões 3.5.0 e superiores do kernel):

`sudo dmesg -w`

- Exibe a quantidade de memória física disponível no sistema:

`sudo dmesg | grep -i memory`

- Exibe as mensagens do kernel divididas em páginas:

`sudo dmesg | less`

- Exibe as menagens do kernel com data/hora (disponível nas versões 3.5.0 e superiores do kernel):

`sudo dmesg -T`

- Exibe as mensagens do kernel em um formato de fácil leitura (disponível nas versões 3.5.0 e superiores do kernel):

`sudo dmesg -H`

- Exibe as mensagens do kernel utilizando cores (disponível nas versões 3.5.0 e superiores do kernel):

`sudo dmesg -L`
