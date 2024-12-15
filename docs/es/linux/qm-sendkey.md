---
layout: page
title: linux/qm-sendkey (español)
description: "Envía un evento de teclado del monitor QEMU a una máquina virtual."
content_hash: f0dabde2ff340f76478c740cdca1802585f9056b
last_modified_at: 2024-12-15
related_topics:
  - title: English version
    url: /en/linux/qm-sendkey.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-sendkey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm sendkey

Envía un evento de teclado del monitor QEMU a una máquina virtual.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Envía el evento de teclado (key) especificado a una máquina virtual específica:

`qm sendkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tecla</span>

- Permite al usuario root enviar el evento clave e ignorar cualquier bloqueo:

`qm sendkey --skiplock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tecla</span>
