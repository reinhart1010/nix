---
layout: page
title: linux/portageq (español)
description: "Consulta información sobre Portage, el gestor de paquetes de Gentoo Linux."
content_hash: 6c0518d27dfdfb3206a939d484e82025341e9667
last_modified_at: 2024-07-08
related_topics:
  - title: English version
    url: /en/linux/portageq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# portageq

Consulta información sobre Portage, el gestor de paquetes de Gentoo Linux.
Las variables de entorno específicas de Portage que se pueden consultar están listadas en `/var/db/repos/gentoo/profiles/info_vars`.
Más información: <https://wiki.gentoo.org/wiki/Portageq>.

- Muestra el valor de una variable de entorno específica de Portage:

`portageq envvar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Muestra una lista detallada de los repositorios configurados con Portage:

`portageq repos_config /`

- Muestra una lista de repositorios ordenados por prioridad (el más alto, primero):

`portageq get_repos /`

- Muestra un fragmento específico de metadatos sobre un átomo (por ejemplo, el nombre del paquete incluyendo la versión):

`portageq metadata / `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ebuild|porttree|binary|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">categoría</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">BDEPEND|DEFINED_PHASES|DEPEND|...</span>
