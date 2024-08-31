---
layout: page
title: linux/slurp (español)
description: "Selecciona una región en un compositor Wayland."
content_hash: 46be5e0dab5c8e798eb0c064468b1abe0787d980
last_modified_at: 2024-08-31
related_topics:
  - title: English version
    url: /en/linux/slurp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# slurp

Selecciona una región en un compositor Wayland.
Más información: <https://github.com/emersion/slurp>.

- Selecciona una región y la imprime en `stdout`:

`slurp`

- Selecciona una región e imprímela en `stdout`, mientras muestras las dimensiones de la selección:

`slurp -d`

- Selecciona un único punto en lugar de una región:

`slurp -p`

- Selecciona una salida e imprime su nombre:

`slurp -o -f '%o'`

- Selecciona una región determinada y hace una captura de pantalla sin bordes utilizando `grim`:

`grim -g "$(slurp -w 0)"`

- Selecciona una región determinada y graba un vídeo sin bordes utilizando `wf-recorder`:

`wf-recorder --geometry "$(slurp -w 0)"`
