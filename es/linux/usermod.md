---
layout: page
title: linux/usermod (español)
description: "Modifica una cuenta de usuario."
content_hash: fbf0995f94a882711141cae52539b98df33efe7b
related_topics:
  - title: English version
    url: /en/linux/usermod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/usermod.html
    icon: bi bi-globe
---
# usermod

Modifica una cuenta de usuario.
Más información: <https://manned.org/usermod>.

- Cambia el nombre de un usuario:

`usermod -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevo_nombre</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Añade un usuario a grupos suplementarios (tener en cuenta los espacios en blanco):

`usermod -a -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo1,grupo2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Crea un nuevo directorio home para un usuario y mueve sus archivos a él:

`usermod -m -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/home</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>
