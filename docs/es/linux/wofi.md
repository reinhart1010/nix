---
layout: page
title: linux/wofi (español)
description: "Un lanzador de aplicaciones para compositores Wayland basados en wlroots, similar a `rofi` y `dmenu`."
content_hash: cc884a029f1744fa81aee04b8d6f7a807ad00334
last_modified_at: 2024-09-12
related_topics:
  - title: English version
    url: /en/linux/wofi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/wofi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wofi

Un lanzador de aplicaciones para compositores Wayland basados en wlroots, similar a `rofi` y `dmenu`.
Más información: <https://hg.sr.ht/~scoopta/wofi>.

- Muestra la lista de aplicaciones:

`wofi --show drun`

- Muestra la lista de todos los comandos:

`wofi --show run`

- Envía una lista de elementos a `stdin` e imprime el elemento seleccionado en `stdout`:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Choice1\nChoice2\nChoice3</span>`" | wofi --dmenu`
