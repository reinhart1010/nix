---
layout: page
title: common/histexpand (español)
description: "Reutiliza y expande el historial del shell en `sh`, `bash`, `zsh`, `rbash` y `ksh`."
content_hash: bdcb15062b7cafd9fe2d67624119c638aa72d036
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/histexpand.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/histexpand.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/histexpand.html
    icon: bi bi-globe
tldri18n_status: 2
---
# history expansion

Reutiliza y expande el historial del shell en `sh`, `bash`, `zsh`, `rbash` y `ksh`.
Más información: <https://www.gnu.org/software/bash/manual/html_node/History-Interaction>.

- Ejecuta el comando anterior como root (`!!` se sustituye por el comando anterior):

`sudo !!`

- Ejecuta un comando con el último argumento del comando anterior:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` !$`

- Ejecuta un comando con el primer argumento del comando anterior:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` !^`

- Ejecuta el `n` comando del historial:

`!`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Ejecuta el comando `n` líneas atrás en el historial:

`!-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Ejecuta el comando más reciente que contenga `cadena`:

`!?`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena</span>`?`

- Ejecuta el comando anterior, sustituyendo "cadena1" por "cadena2":

`^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena1</span>`^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena2</span>`^`

- Realiza una expansión del historial, pero imprimiendo el comando que se ejecutaría en lugar de ejecutarlo realmente:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">!-n</span>`:p`
