---
layout: page
title: linux/qm-start (Deutsch)
description: "Starte eine virtuelle Maschine per QEMU/KVM Virtual Machine Manager."
content_hash: 354fd010ab2f3d2dda576a8e6809355c1e1fddf8
related_topics:
  - title: English version
    url: /en/linux/qm-start.html
    icon: bi bi-globe
---
# qm start

Starte eine virtuelle Maschine per QEMU/KVM Virtual Machine Manager.
Weitere Informationen: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Starte eine bestimmte virtuelle Maschine:

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Lege den QEMU Maschinentyp fest (etwa den zu emulierenden Prozessor):

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">q35</span>

- Starte eine bestimmte virtuelle Maschine mit einem Timeout (Zeitabschaltung) nach 60 Sekunden:

`qm start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>
