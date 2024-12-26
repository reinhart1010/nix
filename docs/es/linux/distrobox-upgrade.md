---
layout: page
title: linux/distrobox-upgrade (español)
description: "Actualiza uno o varios contenedores Distrobox. Vea también: `tldr distrobox`."
content_hash: d7ad88c8557278816f2c56c09fc2e598bd79ee7a
last_modified_at: 2024-12-26
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
tldri18n_status: 2
---
# distrobox-upgrade

Actualiza uno o varios contenedores Distrobox. Vea también: `tldr distrobox`.
Más información: <https://distrobox.it/usage/distrobox-upgrade>.

- Actualiza un contenedor usando el administrador de paquetes nativo del contenedor:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Actualiza todos los contenedores utilizando los administradores de paquetes nativos de cada contenedor:

`distrobox-upgrade --all`

- Actualiza contenedores específicos a través del administrador de paquetes nativo de cada contenedor:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contenedor1 contenedor2 ...</span>
