---
layout: page
title: linux/auditctl (español)
description: "Utilidad para controlar el comportamiento, obtener el estado y gestionar las reglas del Sistema de Auditoría de Linux."
content_hash: b5472b5bdbf21d6dd49a68dd9b8488cafacd9ffd
last_modified_at: 2024-07-13
related_topics:
  - title: English version
    url: /en/linux/auditctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/auditctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># auditctl

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
