---
layout: page
title: linux/dnf (español)
description: "Administrador de paquetes para RHEL, CentOS y Fedora (Reemplaza a yum)."
content_hash: ebc0fbbe6cc6c2537bfcafde8a5f05405b93ae20
related_topics:
  - title: Deutsch version
    url: /de/linux/dnf.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dnf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dnf.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dnf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dnf

Administrador de paquetes para RHEL, CentOS y Fedora (Reemplaza a yum).
Más información: <https://dnf.readthedocs.io>.

- Actualiza todos los paquetes a la última versión disponible:

`sudo dnf update`

- Busca un paquete usando palabras clave:

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clave</span>

- Muestra información acerca de un paquete:

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Instala un nuevo paquete:

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Instala un nuevo paquete respondiendo si a todas las preguntas:

`sudo dnf install -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Lista todos los paquetes instalados:

`dnf list --installed`

- Encuentra que paquete provee un archivo determinado:

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>
