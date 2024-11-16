---
layout: page
title: linux/systemd-sysext (español)
description: "Activa o desactiva imágenes de extensión del sistema (system extension images)."
content_hash: 2cbc3538ba45bd83be7ce8390d53ef9c1f904110
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/linux/systemd-sysext.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/systemd-sysext.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/systemd-sysext.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-sysext.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-sysext

Activa o desactiva imágenes de extensión del sistema (system extension images).
Más información: <https://www.freedesktop.org/software/systemd/man/systemd-sysext.html>.

- Lista de imágenes de extensión instaladas:

`systemd-sysext list`

- Combina imágenes de extensión del sistema en `/usr/` y `/opt/`:

`systemd-sysext merge`

- Comprueba el estado de fusión actual:

`systemd-sysext status`

- Separa todas las imágenes de extensión del sistema actualmente instaladas en `/usr/` y `/opt/`:

`systemd-sysext unmerge`

- Actualiza imágenes de extensión del sistema (una combinación de `unmerge` y `merge`):

`systemd-sysext refresh`
