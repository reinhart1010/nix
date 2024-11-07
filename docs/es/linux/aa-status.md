---
layout: page
title: linux/aa-status (español)
description: "Lista los módulos AppArmor cargados actualmente."
content_hash: e40f424a0e29b3d968559660c8f27544a0756322
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/linux/aa-status.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/aa-status.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aa-status.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-status

Lista los módulos AppArmor cargados actualmente.
Vea también: `aa-complain`, `aa-disable`, `aa-enforce`.
Más información: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>.

- Muestra el estado:

`sudo aa-status`

- Muestra el número de políticas cargadas:

`sudo aa-status --profiled`

- Muestra el número de políticas impuestas cargadas:

`sudo aa-status --enforced`

- Muestra el número de políticas no obligatorias cargadas:

`sudo aa-status --complaining`

- Muestra el número de políticas impuestas cargadas que terminan tareas:

`sudo aa-status --kill`
