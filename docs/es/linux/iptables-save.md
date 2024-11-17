---
layout: page
title: linux/iptables-save (español)
description: "Guarda la configuración IPv4 de `iptables`."
content_hash: 11f14596cefa8f1de0a82e496a242ac503d3b941
last_modified_at: 2024-11-17
related_topics:
  - title: English version
    url: /en/linux/iptables-save.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/iptables-save.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/iptables-save.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/iptables-save.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># iptables-save

Guarda la configuración IPv4 de `iptables`.
Use `ip6tables-save` para hacer lo mismo para IPv6.
Más información: <https://manned.org/iptables-save>.

- Imprime la configuración de `iptables`:

`sudo iptables-save`

- Imprime la configuración de `iptables` de una [t]abla específica:

`sudo iptables-save --table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tabla</span>

- Guarda la configuración de `iptables` al archivo:

`sudo iptables-save --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
