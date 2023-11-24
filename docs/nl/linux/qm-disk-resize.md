---
layout: page
title: linux/qm-disk-resize (Nederlands)
description: "Wijzig de grote van een virtuele machine schijf in the Proxmox Virtual Environment (PVE)."
content_hash: 4bc2e3e704e184a21445a6a5cbf8155ce96af3cd
last_modified_at: 2023-11-24
related_topics:
  - title: English version
    url: /en/linux/qm-disk-resize.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-disk-resize.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm disk resize

Wijzig de grote van een virtuele machine schijf in the Proxmox Virtual Environment (PVE).
Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Voeg `n` gigabytes toe aan een virtuele schijf:

`qm disk resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schijfnaam</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>`G`
