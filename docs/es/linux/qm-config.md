---
layout: page
title: linux/qm-config (español)
description: "Muestra la configuración de la máquina virtual con los cambios de configuración pendientes aplicados."
content_hash: 74e983119a540e5b32b4a7d62dc162176c572ddb
last_modified_at: 2024-12-11
related_topics:
  - title: English version
    url: /en/linux/qm-config.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-config.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-config.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm config

Muestra la configuración de la máquina virtual con los cambios de configuración pendientes aplicados.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Muestra la configuración de la máquina virtual:

`qm config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>

- Muestra los valores de configuración actuales en lugar de los valores pendientes en la máquina virtual:

`qm config --current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>

- Obtiene los valores de configuración de la instantánea (snapshot) dada:

`qm config --snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_instantánea</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>
