---
layout: page
title: common/arp-scan (français)
description: "Envoie des paquets ARP à des hôtes (spécifié via des adresses IP ou des noms de domaines) pour scanner le réseau local."
content_hash: 3c940126ff22ed5c192e3054d04bab60ad2688be
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/arp-scan.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/arp-scan.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arp-scan.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp-scan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arp-scan

Envoie des paquets ARP à des hôtes (spécifié via des adresses IP ou des noms de domaines) pour scanner le réseau local.
Plus d'informations : <https://github.com/royhills/arp-scan>.

- Scanne le réseau local actuel :

`arp-scan --localnet`

- Scanne un réseau IP pour un masque de bits donné :

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>

- Scanne un réseau IP dans une plage IP :

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.0</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.31</span>

- Scanne un réseau IP pour un masque de sous-réseaux donné :

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">255.255.255.0</span>
