---
layout: page
title: linux/ipcalc (Deutsch)
description: "Einfache Operationen und Berechnungen mit IP-Adressen und Netzwerken durchführen."
content_hash: 2a78e7534040212374a1a26a2fb619874c0cc211
related_topics:
  - title: English version
    url: /en/linux/ipcalc.html
    icon: bi bi-globe
---
# ipcalc

Einfache Operationen und Berechnungen mit IP-Adressen und Netzwerken durchführen.
Weitere Informationen: <https://manned.org/ipcalc>.

- Zeige Informationen über eine Adresse oder ein Netzwerk mit einer bestimmten Subnetzmaske an:

`ipcalc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">255.255.255.0</span>

- Zeige Informationen über eine Adresse oder ein Netzwerk in CIDR-Notation an:

`ipcalc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>

- Zeige die Broadcast-Adresse einer Adresse oder eines Netzwerks an:

`ipcalc -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- Zeige die Netzwerkadresse der angegebenen IP-Adresse und Netzmaske an:

`ipcalc -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>

- Zeige geografische Informationen zu einer bestimmten IP-Adresse an:

`ipcalc -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>
