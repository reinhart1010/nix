---
layout: page
title: common/hexyl (español)
description: "Un simple visor hexadecimal para la terminal. Utiliza salida coloreada para distinguir diferentes categorías de bytes."
content_hash: f58cb56b0201dd456231a4fc56cc3ba3d4f879b3
last_modified_at: 2024-02-28
related_topics:
  - title: English version
    url: /en/common/hexyl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/hexyl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hexyl

Un simple visor hexadecimal para la terminal. Utiliza salida coloreada para distinguir diferentes categorías de bytes.
Más información: <https://github.com/sharkdp/hexyl>.

- Imprime la representación hexadecimal de un archivo:

`hexyl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime la representación hexadecimal de los primeros `n` bytes de un archivo:

`hexyl -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime los bytes 512 a 1024 de un archivo:

`hexyl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime 512 bytes empezando por el byte 1024:

`hexyl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>`:+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
