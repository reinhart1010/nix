---
layout: page
title: common/upt (español)
description: "Interfaz unificada para gestionar paquetes en varios sistemas operativos, tales como Windows, diversas distribuciones de Linux, macOS, FreeBSD e incluso Haiku."
content_hash: 566a706fc86b8aae593bb44f5cf087e23b277e3c
last_modified_at: 2024-04-13
related_topics:
  - title: English version
    url: /en/common/upt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# upt

Interfaz unificada para gestionar paquetes en varios sistemas operativos, tales como Windows, diversas distribuciones de Linux, macOS, FreeBSD e incluso Haiku.
Requiere que el gestor de paquetes nativo del sistema operativo esté instalado.
Vea también: `flatpak`, `brew`, `scoop`, `apt`, `dnf`.
Más información: <https://github.com/sigoden/upt>.

- Actualiza la lista de paquetes disponibles:

`upt update`

- Busca un paquete:

`upt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">término_de_búsqueda</span>

- Muestra información sobre un paquete:

`upt info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Instala un paquete:

`upt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete:

`upt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remove|uninstall</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Actualiza todos los paquetes instalados:

`upt upgrade`

- Actualiza un paquete:

`upt upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Lista los paquetes instalados:

`upt list`
