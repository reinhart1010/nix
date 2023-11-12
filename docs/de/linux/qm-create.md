---
layout: page
title: linux/qm-create (Deutsch)
description: "Erzeugung einer virtuellen Maschine per QEMU/KVM Virtual Machine Manager."
content_hash: 9f734ce9d255d6809d019ea327f13051e91ed8fc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/qm-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm create

Erzeugung einer virtuellen Maschine per QEMU/KVM Virtual Machine Manager.
Weitere Informationen: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Erzeuge eine virtuelle Maschine:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Erzeuge eine virtuelle Maschine und starte sie unmittelbar danach im Anschluss:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --start 1`

- Lege den Typ des Betriebssystems auf der virtuellen Maschine fest:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --ostype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">win10</span>

- Ersetze eine bestehende virtuelle Maschine (setzt deren Archivierung voraus):

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/backup_file.tar</span>` --force 1`

- Lege ein Skript fest, welches automatisch abhängig vom Zustand der virtuellen Maschine ausgelöst werden soll:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --hookscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/script.pl</span>
