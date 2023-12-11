---
layout: page
title: linux/yum (español)
description: "Administrador de paquetes para RHEL, CentOS y Fedora (para versiones anteriores)."
content_hash: e1a94f73e1ccc2440372b116e8c7a51fdead9a9a
last_modified_at: 2023-12-11
related_topics:
  - title: català version
    url: /ca/linux/yum.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/yum.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/yum.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/yum.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yum

Administrador de paquetes para RHEL, CentOS y Fedora (para versiones anteriores).
Más información: <https://manned.org/yum>.

- Instala un nuevo paquete:

`yum install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Instala un nuevo paquete respondiendo sí a todas las preguntas (también trabaja con actualizaciones, útil para actualizaciones automáticas):

`yum -y install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Encuentra que paquete provee un archivo determinado:

`yum provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Elimina un paquete:

`yum remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Muestra las actualizaciones disponibles para los paquetes instalados:

`yum check-update`

- Actualiza los paquetes instalados a las versiones más recientes disponibles:

`yum upgrade`
