---
layout: page
title: linux/userdel (català)
description: "Elimina una conta d'usuari o elimina un usuari d'un grup."
content_hash: cd55acc9204828cb56aa8608ac9dbf118fb376a8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/userdel.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/userdel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/userdel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# userdel

Elimina una conta d'usuari o elimina un usuari d'un grup.
Vegeu també: `users`, `useradd`, `usermod`.
Més informació: <https://manned.org/userdel>.

- Elimina un usuari:

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>

- Elimina un usuari en un altre directori root:

`sudo userdel --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/altre/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>

- Elimina un usuari en conjunt amb el seu directori home i mail spool:

`sudo userdel --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>
