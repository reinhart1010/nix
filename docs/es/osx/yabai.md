---
layout: page
title: osx/yabai (español)
description: "Un administrador de ventanas en mosaico para macOS basado en la partición de espacio binario."
content_hash: a23f9b54e04a7db060d611808afc38f0f06072ec
related_topics:
  - title: English version
    url: /en/osx/yabai.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># yabai

Un administrador de ventanas en mosaico para macOS basado en la partición de espacio binario.
Más información: <https://github.com/koekeishiya/yabai>.

- Establece la diposición a bsp:

`yabai -m config layout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bsp</span>

- Establece el espacio de la ventana en 10pt:

`yabai -m config window_gap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Habilita opacidad:

`yabai -m config window_opacity on`

- Deshabilita la sombra de la ventana:

`yabai -m config window_shadow off`

- Habilita la barra de estado:

`yabai -m config status_bar on`
