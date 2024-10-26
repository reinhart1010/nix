---
layout: page
title: linux/userdel (español)
description: "Elimina una cuenta de usuario o elimina un usuario de un grupo."
content_hash: 5b18ec0852edab0e6a8e1a2d5a88babaae98fc7f
last_modified_at: 2024-10-26
related_topics:
  - title: català version
    url: /ca/linux/userdel.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/userdel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/userdel.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/userdel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# userdel

Elimina una cuenta de usuario o elimina un usuario de un grupo.
Vea también: `users`, `useradd`, `usermod`.
Más información: <https://manned.org/userdel>.

- Elimina un usuario:

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Elimina un usuario en otro directorio raíz:

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-R|--root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/otro/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Elimina un usuario junto con su directorio home y correo (mail spool):

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--remove</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>
