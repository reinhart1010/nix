---
layout: page
title: osx/fdesetup (español)
description: "Establece y recupera información relacionada con FileVault."
content_hash: 1638502c5417e6209ba978cd2af284a5372cb6ec
last_modified_at: 2024-01-02
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

- Obtiene el estado actual de FileVault:

`fdesetup status`

- Añade un usuario habilitado para FileVault:

`sudo fdesetup add -usertoadd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario1</span>

- Habilita FileVault:

`sudo fdesetup enable`

- Desactiva FileVault:

`sudo fdesetup disable`
