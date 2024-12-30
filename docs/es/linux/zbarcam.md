---
layout: page
title: linux/zbarcam (español)
description: "Escanea y decodifica códigos de barras (y códigos QR) desde un dispositivo de vídeo."
content_hash: 758160fc433af819e251f1e7b18d996c283b5b46
last_modified_at: 2024-12-30
related_topics:
  - title: English version
    url: /en/linux/zbarcam.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/zbarcam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zbarcam

Escanea y decodifica códigos de barras (y códigos QR) desde un dispositivo de vídeo.
Más información: <https://manned.org/zbarcam>.

- Lee continuamente códigos de barras y los imprime a `stdout`:

`zbarcam`

- Desactiva la ventana de salida de video mientras se escanea:

`zbarcam --nodisplay`

- Imprime códigos de barras sin información de tipo:

`zbarcam --raw`

- Define el dispositivo de captura:

`zbarcam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_de_video</span>
