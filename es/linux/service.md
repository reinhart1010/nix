---
layout: page
title: linux/service (español)
description: "Gestiona los servicios mediante la ejecución de scripts init."
content_hash: ec9d4f87d83e6aeb4e1659fb4b1acd3b2c456186
related_topics:
  - title: English version
    url: /en/linux/service.html
    icon: bi bi-globe
---
# service

Gestiona los servicios mediante la ejecución de scripts init.
Se debe omitir la ruta completa del script (se asume `/etc/init.d/`).

- Lista el nombre y el estado de todos los servicios:

`service --status-all`

- Inicia/Para/Reinicia/Recarga servicio (_start_/_stop_ debería estar siempre disponible):

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_servicio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>

- Hace un reinicio completo (ejecuta el script dos veces con _start_ y _stop_):

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_servicio</span>` --full-restart`

- Muestra el estado actual de un servicio:

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_servicio</span>` status`
