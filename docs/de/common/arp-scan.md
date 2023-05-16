---
layout: page
title: common/arp-scan (Deutsch)
description: "ARP Pakete an Host (spezifiert mit IP Adresse oder Hostname) senden um das lokale Netzwerk zu scannen."
content_hash: 89a172c9b8bbc0618a807f1af2499dc1b87092b6
last_modified_at: 2023-05-16
related_topics:
  - title: English version
    url: /en/common/arp-scan.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arp-scan.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arp-scan.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp-scan.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># arp-scan

ARP Pakete an Host (spezifiert mit IP Adresse oder Hostname) senden um das lokale Netzwerk zu scannen.
Weitere Informationen: <https://github.com/royhills/arp-scan>.

- Scanne das lokale Netzwerk:

`arp-scan --localnet`

- Scanne ein IP Netzwerk mit einer benutzerdefinierten Bitmaske:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">netzwerk_adresse</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">netzwerk_subnet</span>

- Scanne ein IP Netzwerk innerhalb einer benutzerdefinierten Range:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse_a</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse_b</span>

- Scanne ein IP Netzwerk mit einer benutzerdefinierten Netzmaske:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">netzwerkmaske</span>
