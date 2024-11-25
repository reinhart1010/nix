---
layout: page
title: common/pngtopam (español)
description: "Convierte una imagen PNG a una imagen Netpbm."
content_hash: be7c219e0ad75d6732d34edb3e1b7e85a850e892
last_modified_at: 2024-11-25
related_topics:
  - title: English version
    url: /en/common/pngtopam.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pngtopam.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pngtopam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pngtopam

Convierte una imagen PNG a una imagen Netpbm.
Vea también: `pamtopng`.
Más información: <https://netpbm.sourceforge.net/doc/pngtopam.html>.

- Convierte la imagen PNG especificada en imagen Netpbm:

`pngtopam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pam</span>

- Crea una imagen de salida que incluye tanto la imagen principal como la máscara de transparencia de la imagen de entrada:

`pngtopam -alphapam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pam</span>

- Reemplaza píxeles transparentes por el color especificado:

`pngtopam -mix -background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pam</span>

- Escribe los trozos de tEXt encontrados en la imagen de entrada al archivo de texto especificado:

`pngtopam -text `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pam</span>
