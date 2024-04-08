---
layout: page
title: linux/ydotool (español)
description: "Controla las entradas de teclado y ratón mediante comandos de forma agnóstica al servidor de visualización."
content_hash: b2e7ef3f1477c4de64928594b72804e71bca55dd
last_modified_at: 2024-04-08
related_topics:
  - title: English version
    url: /en/linux/ydotool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ydotool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ydotool

Controla las entradas de teclado y ratón mediante comandos de forma agnóstica al servidor de visualización.
Más información: <https://github.com/ReimuNotMoe/ydotool>.

- Inicia el daemon ydotool en segundo plano:

`ydotoold`

- Realiza un clic con el botón izquierdo:

`ydotool click 0xC0`

- Realiza un clic con el botón derecho:

`ydotool click 0xC1`

- Ingresa la combinación de teclas Alt+F4:

`ydotool key 56:1 62:1 62:0 56:0`
