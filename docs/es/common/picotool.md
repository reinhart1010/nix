---
layout: page
title: common/picotool (español)
description: "Gestiona las placas Raspberry Pi Pico."
content_hash: ed9e5a4eda5b14ecb2144e27bdf5d7bae2448d37
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/picotool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# picotool

Gestiona las placas Raspberry Pi Pico.
Más información: <https://github.com/raspberrypi/picotool>.

- Muestra información sobre el programa cargado actualmente en un Pico:

`picotool info`

- Carga un binario en un Pico:

`picotool load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>

- Convierte un archivo ELF o BIN a UF2:

`picotool uf2 convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/elf_o_bin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida</span>

- Reinicia un Pico:

`picotool reboot`

- Lista todos los registros conocidos:

`picotool otp list`

- Muestra la versión:

`picotool version`

- Muestra la ayuda:

`picotool help`
