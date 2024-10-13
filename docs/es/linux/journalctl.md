---
layout: page
title: linux/journalctl (español)
description: "Consulta el registro systemd."
content_hash: aea371ce0b7460e3691e7887fd92723d7202a5a7
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/linux/journalctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/journalctl.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/journalctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# journalctl

Consulta el registro systemd.
Más información: <https://manned.org/journalctl>.

- Muestra todos los mensajes con nivel de prioridad 3 (errores) de este [b]oot:

`journalctl -b --priority=3`

- Elimina los registros diarios con más de 2 días de antigüedad:

`journalctl --vacuum-time=2d`

- Muestra solo las últimas N líneas y sigue los mensajes nuevos (como `tail -f` de un syslog tradicional):

`journalctl --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` --follow`

- Muestra todos los mensajes de una [u]nidad específica:

`journalctl --unit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidad</span>

- Muestra los registros de una unidad determinada desde la última vez que se inició:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidad</span>`)`

- Filtra mensajes dentro de un intervalo de tiempo (marca de tiempo o marcadores de posición como "ayer"):

`journalctl --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">now|today|yesterday|tomorrow</span>` --until "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD HH:MM:SS</span>`"`

- Muestra todos los mensajes de un proceso específico:

`journalctl _PID=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Mostrar todos los mensajes de un ejecutable específico:

`journalctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/ejecutable</span>
