---
layout: page
title: linux/qm-disk-import (español)
description: "Importa una imagen de disco a una máquina virtual como un disco sin utilizar."
content_hash: 29b4bfd20016ffd983d6e68ff91b9bec07ebe109
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/qm-disk-import.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-disk-import.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/qm-disk-import.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-disk-import.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm disk import

Importa una imagen de disco a una máquina virtual como un disco sin utilizar.
Los formatos de imagen que `qemu-img` soporta son: raw, qcow2, qed, vdi, vmdk, y vhd.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Importa una imagen de disco VMDK/qcow2/raw usando un nombre de almacenamiento específico:

`qm importdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/disco</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_disco</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qcow2|raw|vmdk</span>
