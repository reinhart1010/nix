---
layout: page
title: linux/usermod (català)
description: "Modifica una conta d'usuari."
content_hash: 37528362ab991b3d439d0f7126e0ee03abed2fb7
related_topics:
  - title: English version
    url: /en/linux/usermod.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/usermod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/usermod.html
    icon: bi bi-globe
---
# usermod

Modifica una conta d'usuari.
Vegeu també: `users`, `useradd`, `userdel`.
Més informació: <https://manned.org/usermod>.

- Canvia el nom d'usuari:

`sudo_usermod -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nou_nom_usuari</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>

- Canvia l'id d'usuari:

`sudo_usermod --uid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>

- Canvia la shell d'un usuari:

`sudo_usermod --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cami/a/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuar</span>

- Afegeix un usuari a grups suplementaris (cal tenir en compte els espais en blanc):

`sudo_usermod -a -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grup1,grup2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuar</span>

- Crea un nou directori home per un usuari i mou tots els arxius a ell:

`sudo_usermod -m -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/home</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuar</span>
