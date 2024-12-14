---
layout: page
title: linux/qm-vncproxy (español)
description: "Hace proxy de una máquina virtual VNC (Computación virtual de red) enviando tráfico a `stdin` o `stdout`."
content_hash: c3768af96faa56998649cb049a76695fff3314ef
last_modified_at: 2024-12-14
related_topics:
  - title: English version
    url: /en/linux/qm-vncproxy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-vncproxy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-vncproxy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm vncproxy

Hace proxy de una máquina virtual VNC (Computación virtual de red) enviando tráfico a `stdin` o `stdout`.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Hace proxy de una máquina virtual específica:

`qm vncproxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>
