---
layout: page
title: linux/debman (español)
description: "Lee las páginas de ayuda (man) de paquetes desinstalados."
content_hash: 948628bad8da31782a5f33dd7e8885618b4aea33
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/debman.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/debman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debman

Lee las páginas de ayuda (man) de paquetes desinstalados.
Más información: <https://manned.org/debman.1>.

- Lee una página man para un comando proporcionado por un paquete dado:

`debman -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Especifica una versión de paquete a descargar:

`debman -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Lee una página man de un archivo `.deb`:

`debman -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivoname.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
