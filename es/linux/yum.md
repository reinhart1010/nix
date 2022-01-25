---
layout: page
title: linux/yum (español)
description: "Administrador de paquetes para RHEL, CentOS y Fedora (para versiones anteriores)."
content_hash: 5aee7a2755313b8c188b28afc621be378f6262c7
related_topics:
  - title: English version
    url: /en/linux/yum.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/yum.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># yum

Administrador de paquetes para RHEL, CentOS y Fedora (para versiones anteriores).
Más información: <https://manned.org/yum>.

- Instala un nuevo paquete:

`yum install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Instala un nuevo paquete respondiendo si a todas las preguntas (también trabaja con actualizaciones, util para actualizaciones automáticas):

`yum -y install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Encuentra que paquete provee un archivo determinado:

`yum provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Elimina un paquete:

`yum remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Muestra las actualizaciones disponibles para los paquetes instalados:

`yum check-update`

- Actualiza los paquetes instalados a las versiones más recientes disponibles:

`yum upgrade`
