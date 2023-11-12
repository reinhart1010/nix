---
layout: page
title: linux/coredumpctl (català)
description: "Recupera i processa volcats de memòria i les seves metadades."
content_hash: 671936b3ba310dc6a492d112867250533ab8105d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/coredumpctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/coredumpctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/coredumpctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# coredumpctl

Recupera i processa volcats de memòria i les seves metadades.
Més informació: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- Llista tots els volcats de memòria capturats:

`coredumpctl list`

- Llista tots els volcats de memòria capturats per un programa:

`coredumpctl list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Mostra informació sobre els volcats de memòria que coincideixin amb el `PID` d'un programa:

`coredumpctl info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Invoca el depurador fent servir l'últim volcat de memòria per un programa:

`coredumpctl debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Extreu l'últim volcat de memòria a un fitxer:

`coredumpctl --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/arxiu</span>` dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>
