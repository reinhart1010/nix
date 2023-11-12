---
layout: page
title: linux/coredumpctl (español)
description: "Recupera y procesa volcados de memoria y sus metadatos."
content_hash: 8ec7eff9144436ac6c00d7566363d6cebf92e2fc
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/coredumpctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/coredumpctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/coredumpctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# coredumpctl

Recupera y procesa volcados de memoria y sus metadatos.
Más información: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- Lista todos los volcados de memoria capturados:

`coredumpctl list`

- Lista los volcados de memoria capturados para un programa:

`coredumpctl list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Muestra información sobre los volcados de memoria que coincidan con el `PID` de un programa:

`coredumpctl info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Invoca el depurador usando el último volcado de memoria para un programa:

`coredumpctl debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Extrae el último volcado de memoria a un fichero:

`coredumpctl --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>
