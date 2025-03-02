---
layout: page
title: linux/kmod (español)
description: "Gestiona los módulos del kernel de Linux."
content_hash: f1170b75663e474b415343ea41fd8851b5e37e76
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/kmod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kmod

Gestiona los módulos del kernel de Linux.
Este programa es normalmente llamado a través de sus enlaces simbólicos: `lsmod`, `rmmod`, `insmod`, `modinfo`, `modprobe` y `depmod`.
Vea sus respectivas páginas para más información.
Más información: <https://manned.org/kmod>.

- Lista los módulos del núcleo cargados actualmente:

`kmod list`

- Muestra la información de los nodos de dispositivos estáticos proporcionada por los módulos del núcleo que se está ejecutando actualmente:

`kmod static-nodes`
