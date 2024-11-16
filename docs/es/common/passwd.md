---
layout: page
title: common/passwd (español)
description: "Cambia la contraseña de un usuario."
content_hash: e420de0d7a3a26d80f740f94dd4393be45f6ef5d
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/common/passwd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/passwd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/passwd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/passwd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# passwd

Cambia la contraseña de un usuario.
Más información: <https://manned.org/passwd>.

- Cambia la contraseña del usuario actual de forma interactiva:

`passwd`

- Cambia la contraseña de un usuario específico:

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Obtiene el estado actual del usuario:

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-S|--status</span>

- Hace que la contraseña de la cuenta esté en blanco (hará que la cuenta nombrada no tenga contraseña):

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>
