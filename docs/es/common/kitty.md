---
layout: page
title: common/kitty (español)
description: "Un emulador rápido de una terminal basado en GPU rico en características."
content_hash: 195fc15c8630f27ecd3129dcb03ed5fea8a8ae06
last_modified_at: 2024-12-02
related_topics:
  - title: Deutsch version
    url: /de/common/kitty.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/kitty.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/kitty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kitty

Un emulador rápido de una terminal basado en GPU rico en características.
Más información: <https://sw.kovidgoyal.net/kitty/>.

- Abre una nueva terminal:

`kitty`

- Abre una terminal con el título especificado para la ventana:

`kitty --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">título</span>`"`

- Inicia el selector de temas incorporado:

`kitty +kitten themes`

- Muestra una imagen en la terminal:

`kitty +kitten icat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen</span>

- Copia el contenido de `stdin` al portapapeles:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo</span>` | kitty +kitten clipboard`
