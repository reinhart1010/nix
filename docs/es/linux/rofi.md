---
layout: page
title: linux/rofi (español)
description: "Un lanzador de aplicaciones y conmutador de ventanas."
content_hash: c19df1b770020700e3859b0ed5b9da1237e14bf4
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/rofi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rofi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rofi

Un lanzador de aplicaciones y conmutador de ventanas.
Más información: <https://github.com/davatorium/rofi>.

- Muestra la lista de aplicaciones:

`rofi -show drun`

- Muestra la lista de todos los comandos:

`rofi -show run`

- Cambia entre ventanas:

`rofi -show window`

- Envía una lista de elementos a `stdin` y muestra el elemento seleccionado en `stdout`:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Opción1\nOpción2\nOpción3</span>`" | rofi -dmenu`
