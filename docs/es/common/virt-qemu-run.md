---
layout: page
title: common/virt-qemu-run (español)
description: "Herramienta experimental para ejecutar una Guest VM QEMU independiente de `libvirtd`."
content_hash: a0ea4c74e1fdf14fefa682da85242c1a698356bb
last_modified_at: 2024-07-14
related_topics:
  - title: English version
    url: /en/common/virt-qemu-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virt-qemu-run

Herramienta experimental para ejecutar una Guest VM QEMU independiente de `libvirtd`.
Más información: <https://libvirt.org/manpages/virt-qemu-run.html>.

- Ejecuta una máquina virtual QEMU:

`virt-qemu-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/guest.xml</span>

- Ejecuta una máquina virtual QEMU y almacena el estado en un directorio específico:

`virt-qemu-run --root=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/guest.xml</span>

- Ejecuta una máquina virtual QEMU y muestra información detallada sobre el inicio:

`virt-qemu-run --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/guest.xml</span>

- Muestra ayuda:

`virt-qemu-run --help`
