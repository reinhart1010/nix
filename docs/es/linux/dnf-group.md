---
layout: page
title: linux/dnf-group (español)
description: "Gestiona colecciones virtuales de paquetes en sistemas basados en Fedora."
content_hash: 84934c95a65a15ca520e7f724f2b8d0c15c65686
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/linux/dnf-group.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnf group

Gestiona colecciones virtuales de paquetes en sistemas basados en Fedora.
Más información: <https://manned.org/man/dnf-group>.

- Lista los grupos DNF, mostrando el estado de instalado o no en una tabla:

`dnf group list`

- Muestra información del grupo DNF, incluyendo repositorio y paquetes opcionales:

`dnf group info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_grupo</span>

- Instala un grupo DNF:

`dnf group install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_grupo</span>

- Elimina un grupo DNF:

`dnf group remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_grupo</span>

- Actualiza un grupo DNF:

`dnf group upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_grupo</span>
