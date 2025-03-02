---
layout: page
title: linux/steamos-chroot (español)
description: "Cambia el directorio raíz en un entorno SteamOS."
content_hash: 1a2015e92db334aa8d642193b25b3584f442d863
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/steamos-chroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# steamos-chroot

Cambia el directorio raíz en un entorno SteamOS.
Más información: <https://gitlab.com/users/evlaV/projects>.

- Cambia a la otra partición A/B:

`steamos-chroot --partset other`

- Cambia a una partición en otra unidad:

`steamos-chroot --disk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>` --partset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|B</span>

- Muestra la ayuda:

`steamos-chroot --help`
