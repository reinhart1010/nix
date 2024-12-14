---
layout: page
title: linux/qm-wait (español)
description: "Espera hasta que se detenga la máquina virtual."
content_hash: c87d55ce57ab8669eb94c53a0e3071e478335f2c
last_modified_at: 2024-12-14
related_topics:
  - title: English version
    url: /en/linux/qm-wait.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-wait.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm wait

Espera hasta que se detenga la máquina virtual.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Espera hasta que se detenga la máquina virtual:

`qm wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>

- Espera hasta que la máquina virtual se detenga con un tiempo de espera máximo de 10 segundos:

`qm wait --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>

- Envía una solicitud de apagado, luego espera hasta que la máquina virtual se detenga con un tiempo máximo de espera de 10 segundos:

`qm shutdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` && qm wait --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>
