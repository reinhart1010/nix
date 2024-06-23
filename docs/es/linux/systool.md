---
layout: page
title: linux/systool (español)
description: "Vea información de dispositivos del sistema por bus, y clases."
content_hash: 55080728f3f08d5bef8dbb83bc77d82b05847f9a
last_modified_at: 2024-06-23
related_topics:
  - title: English version
    url: /en/linux/systool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systool

Vea información de dispositivos del sistema por bus, y clases.
Este comando es parte del paquete `sysfs`.
Más información: <https://github.com/linux-ras/sysfsutils>.

- Lista todos los atributos de los dispositivos de un bus (ej. `pci`, `usb`). Vea todos los buses usando `ls /sys/bus`:

`systool -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus</span>` -v`

- Lista todos los atributos de una clase de dispositivos (ej. `drm`, `block`). Vea todas las clases usando `ls /sys/class`:

`systool -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clase</span>` -v`

- Mostrar solo los controladores de un bus (ej. `pci`, `usb`):

`systool -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus</span>` -D`
