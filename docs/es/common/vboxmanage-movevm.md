---
layout: page
title: common/vboxmanage-movevm (español)
description: "Mueve una máquina virtual (VM) a una nueva ubicación en el sistema anfitrión."
content_hash: 33049cd95f88cba1b1bcefff549fff071a8e8d82
last_modified_at: 2023-12-24
related_topics:
  - title: English version
    url: /en/common/vboxmanage-movevm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vboxmanage movevm

Mueve una máquina virtual (VM) a una nueva ubicación en el sistema anfitrión.
Más información: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-movevm>.

- Mueve la máquina virtual especificada a la ubicación actual:

`VBoxManage movevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_vm</span>

- Especifica la nueva ubicación (nombre de ruta completo o relativo) de la máquina virtual:

`VBoxManage movevm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_vm</span>` --folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nueva_ubicación</span>
