---
layout: page
title: linux/iptables-restore (español)
description: "Restaura la configuración IPv4 de `iptables`."
content_hash: 785da9b6bd503004845feef99ef2e15703cf5f46
last_modified_at: 2024-11-17
related_topics:
  - title: English version
    url: /en/linux/iptables-restore.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/iptables-restore.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/iptables-restore.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/iptables-restore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># iptables-restore

Restaura la configuración IPv4 de `iptables`.
Use `ip6tables-restore` para hacer lo mismo para IPv6.
Más información: <https://manned.org/iptables-restore>.

- Restaura la configuración `iptables` de un archivo:

`sudo iptables-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
