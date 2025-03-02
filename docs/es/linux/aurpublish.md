---
layout: page
title: linux/aurpublish (español)
description: "Publica paquetes del repositorio de usuarios de Arch."
content_hash: e923949ca09c9b1294ca61a4ce232e23391f4182
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/aurpublish.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aurpublish

Publica paquetes del repositorio de usuarios de Arch.
Más información: <https://github.com/eli-schwartz/aurpublish>.

- Verifica la integridad de `PKGBUILD`, genera `.SRCINFO`, crea una plantilla de mensaje de confirmación y publica el paquete en AUR:

`aurpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_paquete</span>

- Añade githooks al repositorio actual:

`aurpublish setup`
