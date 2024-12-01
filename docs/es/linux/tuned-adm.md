---
layout: page
title: linux/tuned-adm (español)
description: "Gestiona y optimiza los perfiles de ajuste del rendimiento del sistema en Linux."
content_hash: ea682a14947b8d7977cca4588b54ee1c822a70f3
last_modified_at: 2024-12-01
related_topics:
  - title: English version
    url: /en/linux/tuned-adm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/tuned-adm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tuned-adm

Gestiona y optimiza los perfiles de ajuste del rendimiento del sistema en Linux.
Más información: <https://tuned-project.org>.

- Lista de perfiles disponibles:

`tuned-adm list`

- Muestra el perfil activo actual:

`tuned-adm active`

- Establece un perfil de ajuste específico:

`tuned-adm profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_perfil</span>

- Recomienda un perfil adecuado en función del sistema actual:

`tuned-adm recommend`

- Desactiva la configuración:

`tuned-adm off`
