---
layout: page
title: linux/qm-resume (español)
description: "Reanuda una máquina virtual."
content_hash: c6c80a5d49128f87bebda2fe39f441baf5802abb
last_modified_at: 2024-12-13
related_topics:
  - title: English version
    url: /en/linux/qm-resume.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-resume.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qm resume

Reanuda una máquina virtual.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Reanuda una máquina virtual dada:

`qm resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>

- Recupera una máquina virtual específica omitiendo cualquier bloqueo (requiere root):

`sudo qm resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` --skiplock true`
