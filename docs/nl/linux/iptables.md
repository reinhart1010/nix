---
layout: page
title: linux/iptables (Nederlands)
description: "Configureer tabellen, ketens en regels van de Linux kernel IPv4 firewall."
content_hash: 24d5c067db3cbbfe1adfc4885d8908f405e6f36f
last_modified_at: 2025-01-03
related_topics:
  - title: English version
    url: /en/linux/iptables.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/iptables.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/iptables.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/iptables.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/iptables.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iptables

Configureer tabellen, ketens en regels van de Linux kernel IPv4 firewall.
Gebruik `ip6tables` om regels in te stellen voor IPv6 verkeer. Bekijk ook: `iptables-save`, `iptables-restore`.
Meer informatie: <https://manned.org/iptables>.

- Bekijk ketens, regels, pakket/byte tellers en regelnummers voor de filter tabel:

`sudo iptables --verbose --numeric --list --line-numbers`

- Zet keten [P]olicy regel:

`sudo iptables --policy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keten</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regel</span>

- Voeg regel toe aan keten policy voor IP:

`sudo iptables --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keten</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regel</span>

- Voeg regel toe aan keten policy voor IP met [p]rotocol en poort in overweging:

`sudo iptables --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keten</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|icmp|...</span>` --dport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regel</span>

- Voeg een NAT regel toe om al het verkeer van `192.168.0.0/24` subnet te vertalen naar de host's publieke IP:

`sudo iptables --table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nat</span>` --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POSTROUTING</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.0/24</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MASQUERADE</span>

- Verwij[D]er keten regel:

`sudo iptables --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keten</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regelnummer</span>
