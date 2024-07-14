---
layout: page
title: linux/auditctl (español)
description: "Utilidad para controlar el comportamiento, obtener el estado y gestionar las reglas del Sistema de Auditoría de Linux."
content_hash: b5472b5bdbf21d6dd49a68dd9b8488cafacd9ffd
last_modified_at: 2024-07-14
related_topics:
  - title: English version
    url: /en/linux/auditctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# auditctl

Utilidad para controlar el comportamiento, obtener el estado y gestionar las reglas del Sistema de Auditoría de Linux.
Más información: <https://manned.org/auditctl>.

- Muestra el e[s]tado del sistema de auditoría:

`sudo auditctl -s`

- Muestra todas las reglas de auditoría cargadas actualmente:

`sudo auditctl -l`

- Elimina todas las reglas de auditoría:

`sudo auditctl -D`

- Habilita/deshabilita el sistema de auditoría:

`sudo auditctl -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|0</span>

- Vigila un archivo en busca de cambios:

`sudo auditctl -a always,exit -F arch=b64 -F path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/al/archivo</span>` -F perm=wa`

- Busca cambios en un directorio de forma recursiva:

`sudo auditctl -a always,exit -F arch=b64 -F dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/al/directorio/</span>` -F perm=wa`

- Muestra ayuda:

`auditctl -h`
