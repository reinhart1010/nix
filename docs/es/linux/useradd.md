---
layout: page
title: linux/useradd (español)
description: "Crea un usuario nuevo."
content_hash: fbf3cbfc3d9adc311e12cddc6d2dcd77c0aed0b3
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/useradd.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/useradd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/useradd.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># useradd

Crea un usuario nuevo.
Más información: <https://manned.org/useradd>.

- Crea un usuario nuevo:

`useradd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Crea un usuario nuevo con el directorio home predeterminado:

`useradd --create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Crea un usuario nuevo con una shell específica:

`useradd --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Crea un usuario nuevo perteneciente a grupos adicionales (tener en cuenta que no existen espacios en blanco):

`useradd --groups `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo1,grupo2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Crea un usuario nuevo del sistema sin directorio home:

`useradd --no-create-home --system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>
