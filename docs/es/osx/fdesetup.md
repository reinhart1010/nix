---
layout: page
title: osx/fdesetup (español)
description: "Establece y recupera información relacionada con FileVault."
content_hash: ba7d3901ec77d08dc8ff66d6f17c222f5a8189a6
last_modified_at: 2024-01-07
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

- Lista los usuarios actuales habilitados para FileVault:

`sudo fdesetup list`

- Obtén el estado actual de FileVault:

`fdesetup status`

- Añade un usuario habilitado para FileVault:

`sudo fdesetup add -usertoadd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario1</span>

- Habilita FileVault:

`sudo fdesetup enable`

- Desactiva FileVault:

`sudo fdesetup disable`
