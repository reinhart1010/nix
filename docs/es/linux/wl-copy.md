---
layout: page
title: linux/wl-copy (español)
description: "Limpia y copia al portapapeles de Wayland."
content_hash: 85c9a3c7be03ffda2bb9c998c34445ee01bb3f22
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/linux/wl-copy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/wl-copy.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/wl-copy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wl-copy

Limpia y copia al portapapeles de Wayland.
Vea también: `wl-paste`, `xclip`.
Más información: <https://github.com/bugaevc/wl-clipboard>.

- Copia el texto al portapapeles:

`wl-copy "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto</span>`"`

- Envía la salida del comando (`ls`) al portapapeles:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>` | wl-copy`

- Copia solo para pegar una única vez y luego lo limpia:

`wl-copy --paste-once "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto</span>`"`

- Copia una imagen:

`wl-copy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen</span>

- Limpia el portapapeles:

`wl-copy --clear`
