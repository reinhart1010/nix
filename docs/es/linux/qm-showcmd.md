---
layout: page
title: linux/qm-showcmd (español)
description: "Muestra la línea de comandos que se utiliza para iniciar una máquina virtual (información de depuración)."
content_hash: 065628a4f49a0ad14e835e62034f55a79b50d239
last_modified_at: 2024-12-15
related_topics:
  - title: English version
    url: /en/linux/qm-showcmd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-showcmd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm showcmd

Muestra la línea de comandos que se utiliza para iniciar una máquina virtual (información de depuración).
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Muestra la línea de comando inicial de una máquina virtual específica:

`qm showcmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>

- Pone cada opción en una nueva línea para mejorar la legibilidad:

`qm showcmd --pretty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>

- Obtiene valores de configuración de una instantánea específica:

`qm showcmd --snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>
