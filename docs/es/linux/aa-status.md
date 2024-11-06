---
layout: page
title: linux/aa-status (español)
description: "Lista los módulos AppArmor cargados actualmente."
content_hash: e40f424a0e29b3d968559660c8f27544a0756322
last_modified_at: 2024-11-06
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/aa-status.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aa-status

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
