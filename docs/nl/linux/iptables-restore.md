---
layout: page
title: linux/iptables-restore (Nederlands)
description: "Herstel de `iptables` IPv4 configuratie."
content_hash: 2bf2b40a5df0aa8bc6ece6c31dbaf9f5cac361a9
last_modified_at: 2023-11-07
related_topics:
  - title: English version
    url: /en/linux/iptables-restore.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># iptables-restore

Herstel de `iptables` IPv4 configuratie.
Gebruik `ip6tables-restore` om hetzelfde te doen voor IPv6.
Meer informatie: <https://manned.org/iptables-restore>.

- Herstel de `iptables` configuratie vanuit een bestand:

`sudo iptables-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
