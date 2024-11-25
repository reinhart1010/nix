---
layout: page
title: common/npm-owner (español)
description: "Gestiona la propiedad de paquetes publicados."
content_hash: b1689414ec2ef8eff35c314e4a872f4da97278e9
last_modified_at: 2024-11-25
related_topics:
  - title: English version
    url: /en/common/npm-owner.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/npm-owner.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/npm-owner.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm owner

Gestiona la propiedad de paquetes publicados.
Más información: <https://docs.npmjs.com/cli/commands/npm-owner>.

- Añade un nuevo usuario como un mantenedor de un paquete:

`npm owner add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_paquete</span>

- Elimina un usuario de la lista de propietarios de un paquete:

`npm owner rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_paquete</span>

- Lista todos los propietarios de un paquete:

`npm owner ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_paquete</span>
