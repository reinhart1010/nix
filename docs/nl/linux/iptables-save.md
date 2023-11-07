---
layout: page
title: linux/iptables-save (Nederlands)
description: "Sla de `iptables` IPv4 configuratie op."
content_hash: fb4655ed59398d203f4a7364239c57d3a5a28f0f
last_modified_at: 2023-11-07
related_topics:
  - title: English version
    url: /en/linux/iptables-save.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># iptables-save

Sla de `iptables` IPv4 configuratie op.
Gebruik `ip6tables-save` om hetzelfde te doen voor IPv6.
Meer informatie: <https://manned.org/iptables-save>.

- Toon de `iptables` configuratie:

`sudo iptables-save`

- Toon de `iptables` configuratie van een specifiek [t]abel:

`sudo iptables-save --table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tabel</span>

- Sla de `iptables` configuratie op in een bestand:

`sudo iptables-save --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
