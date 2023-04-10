---
layout: page
title: common/arp (italiano)
description: "Mostra e gestisci la cache ARP di sistema."
content_hash: b31ccebba63666e9fed0817cd43391ac4e66f9f9
last_modified_at: 2023-04-10
related_topics:
  - title: English version
    url: /en/common/arp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arp.html
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
  - title: Türkçe version
    url: /tr/common/arp.html
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

- Elimina una specifica voce:

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo</span>

- Crea una nuova voce:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_mac</span>
