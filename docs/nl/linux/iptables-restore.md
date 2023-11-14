---
layout: page
title: linux/iptables-restore (Nederlands)
description: "Herstel de `iptables` IPv4 configuratie."
content_hash: 2bf2b40a5df0aa8bc6ece6c31dbaf9f5cac361a9
last_modified_at: 2023-11-14
related_topics:
  - title: English version
    url: /en/linux/iptables-restore.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/iptables-restore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># iptables-restore

Herstel de `iptables` IPv4 configuratie.
Gebruik `ip6tables-restore` om hetzelfde te doen voor IPv6.
Meer informatie: <https://manned.org/iptables-restore>.

- Herstel de `iptables` configuratie vanuit een bestand:

`sudo iptables-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
