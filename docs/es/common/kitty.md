---
layout: page
title: common/kitty (español)
description: "Un emulador rápido de una terminal basado en GPU rico en características."
content_hash: 195fc15c8630f27ecd3129dcb03ed5fea8a8ae06
last_modified_at: 2024-12-01
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kitty.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kitty

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
