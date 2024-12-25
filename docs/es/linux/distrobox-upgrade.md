---
layout: page
title: linux/distrobox-upgrade (español)
description: "Actualiza uno o varios contenedores Distrobox. Vea también: `tldr distrobox`."
content_hash: d7ad88c8557278816f2c56c09fc2e598bd79ee7a
last_modified_at: 2024-12-25
related_topics:
  - title: English version
    url: /en/linux/distrobox-upgrade.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/distrobox-upgrade.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-upgrade.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-upgrade.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/distrobox-upgrade.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># distrobox-upgrade

Actualiza uno o varios contenedores Distrobox. Vea también: `tldr distrobox`.
Más información: <https://distrobox.it/usage/distrobox-upgrade>.

- Actualiza un contenedor usando el administrador de paquetes nativo del contenedor:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Actualiza todos los contenedores utilizando los administradores de paquetes nativos de cada contenedor:

`distrobox-upgrade --all`

- Actualiza contenedores específicos a través del administrador de paquetes nativo de cada contenedor:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contenedor1 contenedor2 ...</span>
