---
layout: page
title: osx/fdesetup (español)
description: "Establece y recupera información relacionada con FileVault."
content_hash: e15d44a1b00c41d76d87e28d2160039c2dea768c
last_modified_at: 2024-01-31
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
Más información: <https://keith.github.io/xcode-man-pages/fdesetup.8.html>.

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
