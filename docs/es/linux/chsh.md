---
layout: page
title: linux/chsh (español)
description: "Cambia el intérprete de comandos de inicio de sesión del usuario."
content_hash: 20d6a731c3c9b03b2c7bf13b257b28c3b3a606cd
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/chsh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/chsh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/chsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chsh

Cambia el intérprete de comandos de inicio de sesión del usuario.
Parte de `util-linux`.
Más información: <https://manned.org/chsh>.

- Establece un intérprete de comandos de inicio de sesión específico para el usuario actual de forma interactiva:

`chsh`

- Establece un intérprete de comandos [s]hell de inicio de sesión específico para el usuario actual:

`chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/shell</span>

- Establecer un inicio de sesión del [s]hell para un usuario específico:

`sudo chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>
