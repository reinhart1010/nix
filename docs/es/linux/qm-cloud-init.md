---
layout: page
title: linux/qm-cloud-init (español)
description: "Configuración de ajustes de cloudinit para máquinas virtuales gestionadas por Ambiente Virtual Proxmox (Virtual Environment) (PVE)."
content_hash: 37d8151d3c7abe7045acf567765be347d3667892
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/linux/qm-cloud-init.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-cloud-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm cloud init

Configuración de ajustes de cloudinit para máquinas virtuales gestionadas por Ambiente Virtual Proxmox (Virtual Environment) (PVE).
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Configura ajustes de cloudinit para un usuario específico y establece una contraseña para el mismo:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` -user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` -password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>

- Configura ajustes de cloudinit para un usuario específico y le establece una contraseña con una clave SSH específica:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` -user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` -password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` -sshkey=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave_ssh</span>

- Establece el nombre de host para una máquina virtual específica:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` -hostname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_equipo</span>

- Configura los ajustes de interfaz de red para una máquina virtual específica:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` -ipconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ipconfig</span>

- Configura un script de interfaz de comandos (shell) para ejecutarse antes de que `cloud-ini` se ejecute en una máquina virtual:

`qm cloud-init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` -pre `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script</span>
