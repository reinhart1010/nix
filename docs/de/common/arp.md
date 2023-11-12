---
layout: page
title: common/arp (Deutsch)
description: "Den ARP Cache des Systems anzeigen und manipulieren."
content_hash: 23ad4b2f1f0aadc9e85c843af7b73dc8cf72b54b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/arp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arp.html
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
  - title: português (Brasil) version
    url: /pt_BR/common/arp.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/arp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># arp

Den ARP Cache des Systems anzeigen und manipulieren.
Weitere Informationen: <https://manned.org/arp>.

- Zeige die aktuelle ARP Tabelle an:

`arp -a`

- Leere den gesamten Cache:

`sudo arp -a -d`

- Lösche einen spezifischen Eintrag in der Tabelle:

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">addresse</span>

- Erstelle einen Eintrag in der ARP Tabelle:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_adresse</span>
