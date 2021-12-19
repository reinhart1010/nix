---
layout: page
title: linux/userdel (español)
description: "Elimina una cuenta de usuario o elimina un usuario de un grupo."
content_hash: 8f5d723d4b5f10faf1bc5d7a23a9ae6a5b1cef4b
related_topics:
  - title: English version
    url: /en/linux/userdel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/userdel.html
    icon: bi bi-globe
---
# userdel

Elimina una cuenta de usuario o elimina un usuario de un grupo.
Nota: todos los comandos deben ser ejecutados como root.
Más información: <https://manned.org/userdel>.

- Elimina un usuario:

`userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Elimina un usuario junto con su directorio home y mail spool:

`userdel --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Elimina un usuario de un grupo:

`userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo</span>

- Elimina un usuario en otro directorio root:

`userdel --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/otro/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>
