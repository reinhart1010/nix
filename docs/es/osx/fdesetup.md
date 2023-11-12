---
layout: page
title: osx/fdesetup (español)
description: "Establece y recupera información relacionada con FileVault."
content_hash: 2b58a3378478aa69bfe0beb359e6c362d5fb8bc7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/fdesetup.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/fdesetup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fdesetup

Establece y recupera información relacionada con FileVault.
Más información: <https://www.unix.com/man-page/mojave/8/fdesetup/>.

- Lista los usuarios actuales habilitados por FileVault:

`sudo fdesetup list`

- Obtiene el estado actual de FileVault:

`fdesetup status`

- Añade un usuario habilitado para FileVault:

`sudo fdesetup add -usertoadd usuario1`

- Habilita FileVault:

`sudo fdesetup enable`

- Desactiva FileVault:

`sudo fdesetup disable`
