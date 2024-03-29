---
layout: page
title: osx/ftxdiff (español)
description: "Compara las diferencias entre dos fuentes."
content_hash: c17153eada7fa760fa72890c5b23b8f4f5139b38
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/osx/ftxdiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ftxdiff

Compara las diferencias entre dos fuentes.
Más información: <https://developer.apple.com/fonts>.

- Envía las diferencias a un archivo de texto específico:

`ftxdiff --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_fontdif.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_ont_1.ttc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_font_2.ttc</span>

- Incluye nombres de glifos en la salida:

`ftxdiff --include-glyph-names`

- Incluye nombres unicode en la salida:

`ftxdiff --include-unicode-names`
