---
layout: page
title: linux/yum (español)
description: "Administrador de paquetes para RHEL, CentOS y Fedora (para versiones anteriores)."
content_hash: 037312cdc71cb2791a9b016152a8ca33ec189fff
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
  - title: português (Brasil) version
    url: /pt_BR/linux/yum.html
    icon: bi bi-globe
---
# yum

Administrador de paquetes para RHEL, CentOS y Fedora (para versiones anteriores).
Más información: <https://manned.org/yum>.

- Instala un nuevo paquete:

`yum install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Instala un nuevo paquete respondiendo sí a todas las preguntas (también trabaja con actualizaciones, útil para actualizaciones automáticas):

`yum -y install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Encuentra que paquete provee un archivo determinado:

`yum provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Elimina un paquete:

`yum remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Muestra las actualizaciones disponibles para los paquetes instalados:

`yum check-update`

- Actualiza los paquetes instalados a las versiones más recientes disponibles:

`yum upgrade`
