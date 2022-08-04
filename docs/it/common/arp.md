---
layout: page
title: common/arp (italiano)
description: "Mostra e gestisci la cache ARP di sistema."
content_hash: cca62a87a5c249d2bfdb57edcbea127eef39188c
related_topics:
  - title: English version
    url: /en/common/arp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/arp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp.html
    icon: bi bi-globe
---
# arp

Mostra e gestisci la cache ARP di sistema.
Maggiori informazioni: <https://manned.org/arp>.

- Mostra la tabella ARP corrente:

`arp -a`

- Elimina l'intera cache:

`sudo arp -a -d`

- Elimina una specifica voce:

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo</span>

- Crea una nuova voce:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_mac</span>
