---
layout: page
title: linux/check-dfsg-status (español)
description: "Informa de paquetes no libres instalados en sistemas operativos basados en Debian."
content_hash: f522911cbf46763691fb5147b44823ee83dcea3d
last_modified_at: 2024-03-04
related_topics:
  - title: English version
    url: /en/linux/check-dfsg-status.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/check-dfsg-status.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># check-dfsg-status

Informa de paquetes no libres instalados en sistemas operativos basados en Debian.
Este comando se conocía anteriormente como `vrms`.
Más información: <https://debian.pages.debian.net/check-dfsg-status/>.

- Lista los paquetes no libres y `contrib` (más la descripción):

`check-dfsg-status`

- Muestra solo los nombres de los paquetes:

`check-dfsg-status --sparse`
