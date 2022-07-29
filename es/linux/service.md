---
layout: page
title: linux/service (español)
description: "Gestiona los servicios mediante la ejecución de scripts init."
content_hash: 55302bdd7850cad421df1a64c91c5e6964636f40
related_topics:
  - title: català version
    url: /ca/linux/service.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/service.html
    icon: bi bi-globe
---
# service

Gestiona los servicios mediante la ejecución de scripts init.
Se debe omitir la ruta completa del script (se asume `/etc/init.d/`).
Más información: <https://manned.org/service>.

- Lista el nombre y el estado de todos los servicios:

`service --status-all`

- Inicia/Para/Reinicia/Recarga servicio (_start_/_stop_ debería estar siempre disponible):

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_servicio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>

- Hace un reinicio completo (ejecuta el script dos veces con _start_ y _stop_):

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_servicio</span>` --full-restart`

- Muestra el estado actual de un servicio:

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_servicio</span>` status`
