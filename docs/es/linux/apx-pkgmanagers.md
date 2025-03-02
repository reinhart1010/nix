---
layout: page
title: linux/apx-pkgmanagers (español)
description: "Administra gestores de paquetes en `apx`."
content_hash: 10c46a1ade62bca25c6744eabcd6c32e5016ba9e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/apx-pkgmanagers.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/apx-pkgmanagers.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apx-pkgmanagers.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apx pkgmanagers

Administra gestores de paquetes en `apx`.
Nota: las configuraciones de gestores de paquetes creadas por el usuario se almacenan en `~/.local/share/apx/pkgmanagers`.
Más información: <https://github.com/Vanilla-OS/apx>.

- Crea de forma interactiva una nueva configuración de gestor de paquetes:

`apx pkgmanagers create`

- Muestra la lista de todas las configuraciones de gestores de paquetes disponibles:

`apx pkgmanagers list`

- Elimina una configuración de gestor de paquetes:

`apx pkgmanagers rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_de_caracteres</span>

- Muestra información sobre un gestor de paquetes específico:

`apx pkgmanagers show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>
