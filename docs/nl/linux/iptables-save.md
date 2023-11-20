---
layout: page
title: linux/iptables-save (Nederlands)
description: "Sla de `iptables` IPv4 configuratie op."
content_hash: fb4655ed59398d203f4a7364239c57d3a5a28f0f
last_modified_at: 2023-11-20
related_topics:
  - title: English version
    url: /en/linux/iptables-save.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/iptables-save.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
