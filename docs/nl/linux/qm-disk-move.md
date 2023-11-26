---
layout: page
title: linux/qm-disk-move (Nederlands)
description: "Verplaats een virtuele schijf van de ene opslag naar de andere binnen hetzelfde Proxmox cluster."
content_hash: 044811fbf82325a2163f8cc61c0bfdb9a9880458
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/linux/qm-disk-move.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-disk-move.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm disk move

Verplaats een virtuele schijf van de ene opslag naar de andere binnen hetzelfde Proxmox cluster.
Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Verplaats een virtuele schijf:

`qm disk move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestemming</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index</span>

- Verwijder de vorige kopie van de virtuele schijf:

`qm disk move -delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestemming</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index</span>
