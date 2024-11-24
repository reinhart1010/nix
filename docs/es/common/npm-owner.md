---
layout: page
title: common/npm-owner (español)
description: "Gestiona la propiedad de paquetes publicados."
content_hash: b1689414ec2ef8eff35c314e4a872f4da97278e9
last_modified_at: 2024-11-24
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-owner.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm owner

Gestiona la propiedad de paquetes publicados.
Más información: <https://docs.npmjs.com/cli/commands/npm-owner>.

- Añade un nuevo usuario como un mantenedor de un paquete:

`npm owner add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_paquete</span>

- Elimina un usuario de la lista de propietarios de un paquete:

`npm owner rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_paquete</span>

- Lista todos los propietarios de un paquete:

`npm owner ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_paquete</span>
