---
layout: page
title: linux/qm-rescan (español)
description: "Revisa de nuevo (rescan) todos los almacenamientos (storages) y actualiza los tamaños de discos e imágenes de disco no utilizadas de una máquina virtual."
content_hash: 908fcada4f54cc2f8eedfcf5da1ce9eac30d9375
last_modified_at: 2024-12-13
related_topics:
  - title: English version
    url: /en/linux/qm-rescan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-rescan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm rescan

Revisa de nuevo (rescan) todos los almacenamientos (storages) y actualiza los tamaños de discos e imágenes de disco no utilizadas de una máquina virtual.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Restaura todos los almacenamientos y actualiza los tamaños de disco e imágenes de disco no utilizadas de la máquina virtual indicada:

`qm rescan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>

- Realiza una simulación de rescan en una máquina virtual específica y no escribe ningún cambio en las configuraciones:

`qm rescan --dryrun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>
