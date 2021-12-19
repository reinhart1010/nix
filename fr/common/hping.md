---
layout: page
title: common/hping (français)
description: "Outil en ligne de commande permettant d'assembler ou analyser des paquets TCP/IP."
content_hash: 7742821f64923486b41fd486a14f97a8ff6461bc
related_topics:
  - title: English version
    url: /en/common/hping.html
    icon: bi bi-globe
---
# hping

Outil en ligne de commande permettant d'assembler ou analyser des paquets TCP/IP.
Inspirer par la commande `ping`.
Plus d'informations : <http://www.hping.org>.

- Ping localhost via TCP :

`hping3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>

- Ping une adresse IP, via TCP, sur un port spécifique :

`hping3 -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>

- Ping une adresse IP, via UDP, sur le port 80 :

`hping3 --udp -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>

- Scanner un ensemble de ports TCP, sur une adresse IP spécifique :

`hping3 --scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,3000,9000</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>

- Effectuer un test de montée en charge sur le port 80 :

`hping3 --flood -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>
