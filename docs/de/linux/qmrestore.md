---
layout: page
title: linux/qmrestore (Deutsch)
description: "Wiederherstellung von QemuServer vzdump Backups."
content_hash: 7785b43653639eefb6e834b3c99a4bc23b5b14a3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/qmrestore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qmrestore

Wiederherstellung von QemuServer vzdump Backups.
Weitere Informationen: <https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- Wiederherstellung einer virtuellen Maschine mittels Backupdatei auf dem ursprünglichen Speicher:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Überschreibung einer bestehenden virtuellen Maschine auf dem ursprünglichen Speicher:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --force true`

- Wiederherstellung einer virtuellen Maschine auf einem bestimmten Speicher:

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --storage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local</span>

- Sofortiger Start einer virtuellen Maschine bei gleichzeitiger Wiederherstellung im Hintergrund (nur bei Proxmox Backup Server):

`qmrestore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/vzdump-qemu-100.vma.lzo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --live-restore true`
