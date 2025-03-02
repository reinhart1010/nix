---
layout: page
title: linux/aurvote (español)
description: "Vota por paquetes en el repositorio de usuarios de Arch (AUR)."
content_hash: 00eeaf7783fb2a95886ca5891d7e0a55b9b87392
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/aurvote.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/aurvote.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aurvote.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aurvote

Vota por paquetes en el repositorio de usuarios de Arch (AUR).
Para poder votar, el archivo `~/.config/aurvote` debe existir y contener tus credenciales del AUR.
Más información: <https://github.com/archlinuxfr/aurvote>.

- Crea interactivamente el archivo `~/.config/aurvote` que contiene su nombre de usuario y contraseña del AUR:

`aurvote --configure`

- Vota por uno o más paquetes del AUR:

`aurvote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Retira el voto de uno o más paquetes del AUR:

`aurvote --unvote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Verifica si uno o más paquetes del AUR ya han sido votados:

`aurvote --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Muestra la ayuda:

`aurvote --help`
