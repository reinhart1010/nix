---
layout: page
title: common/passwd (español)
description: "Cambia la contraseña de un usuario."
content_hash: 9a4ed4d5b9adbe93837ca15178dae26087f60aac
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/passwd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/passwd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/passwd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/passwd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># passwd

Cambia la contraseña de un usuario.
Más información: <https://manned.org/passwd>.

- Cambia la contraseña del usuario actual de forma interactiva:

`passwd`

- Cambia la contraseña de un usuario específico:

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_usuario</span>

- Obtiene el estado actual del usuario:

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-S|--status</span>

- Hace que la contraseña de la cuenta esté en blanco (hará que la cuenta nombrada no tenga contraseña):

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>
