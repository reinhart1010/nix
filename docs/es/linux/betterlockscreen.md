---
layout: page
title: linux/betterlockscreen (español)
description: "Pantalla de bloqueo simple y mínima."
content_hash: 9a855642586a0a00c327326eac96a6cb80607c39
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/linux/betterlockscreen.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/betterlockscreen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# betterlockscreen

Pantalla de bloqueo simple y mínima.
Más información: <https://github.com/betterlockscreen/betterlockscreen>.

- Bloquea la pantalla:

`betterlockscreen --lock`

- Cambia el fondo de la pantalla de bloqueo:

`betterlockscreen -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.png</span>

- Bloquea la pantalla y muestra un texto personalizado:

`betterlockscreen -l pixel -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto de pantalla de bloqueo personalizado</span>`"`

- Bloquea la pantalla, con un tiempo de espera personalizado para apagar el monitor en segundos:

`betterlockscreen --off `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -l`
