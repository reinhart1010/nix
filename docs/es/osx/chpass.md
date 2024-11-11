---
layout: page
title: osx/chpass (español)
description: "Añade o cambia la información de la base de datos del usuario, incluyendo el intérprete de comandos (shell) y la contraseña."
content_hash: 6cf544b91dbcd24b8eb5fb83edcd23c9fb11768a
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/osx/chpass.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/chpass.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/chpass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chpass

Añade o cambia la información de la base de datos del usuario, incluyendo el intérprete de comandos (shell) y la contraseña.
Nota: no es posible cambiar la contraseña del usuario en sistemas Open Directory, utiliza `passwd` en su lugar.
Vea también: `passwd`.
Más información: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Añade o cambia la información de la base de datos del usuario actual de forma interactiva:

`su -c chpass`

- Establece un [s]hell de inicio de sesión específico para el usuario actual:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/shell</span>

- Establece un inicio de sesión [s]hell para un usuario específico:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Edita el registro de usuario en el nodo de directorio en la ubicación dada:

`chpass -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Utiliza el [u]suario_autenticado al identificarse en el nodo de directorio que contiene a cierto usuario:

`chpass -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario_autenticado</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>
