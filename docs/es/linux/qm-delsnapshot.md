---
layout: page
title: linux/qm-delsnapshot (español)
description: "Elimina instantáneas (snapshots) de máquinas virtuales."
content_hash: a5ab7b8f04488421109b60d14ca713ea8e12960b
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/linux/qm-delsnapshot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-delsnapshot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm delsnapshot

Elimina instantáneas (snapshots) de máquinas virtuales.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Elimina una instantánea:

`qm delsnapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_instantánea</span>

- Elimina una instantánea de un archivo de configuración (incluso si la eliminación del disco de la instantánea falla):

`qm delsnapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_instantánea</span>` --force 1`
