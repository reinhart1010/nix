---
layout: page
title: linux/qm-snapshot (español)
description: "Crea instantáneas de máquinas virtuales."
content_hash: 96d20dfc472957bff0c62d6ad8f37b6d7bc74dd0
last_modified_at: 2024-12-16
related_topics:
  - title: English version
    url: /en/linux/qm-snapshot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-snapshot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-snapshot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm snapshot

Crea instantáneas de máquinas virtuales.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Crea una instantánea de una máquina virtual dada:

`qm snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_instantánea</span>

- Crea una instantánea con una descripción dada:

`qm snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_instantánea</span>` --description `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">descripción</span>

- Crea una instantánea incluyendo el vmstate:

`qm snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_instantánea</span>` --description `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">descripción</span>` --vmstate 1`
