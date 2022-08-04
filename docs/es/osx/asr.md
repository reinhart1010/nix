---
layout: page
title: osx/asr (español)
description: "Restaura (copia) una imagen de disco en un volumen."
content_hash: 21863c571ec7fd448ff681134f89275f406c1587
related_topics:
  - title: English version
    url: /en/osx/asr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/asr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/asr.html
    icon: bi bi-globe
---
# asr

Restaura (copia) una imagen de disco en un volumen.
El nombre del comando significa Restauración de Software de Apple.
Más información: <https://www.unix.com/man-page/osx/8/asr/>.

- Restaura una imagen de disco en un volumen:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_imagen</span>`.dmg --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/volumen</span>

- Borra el volumen deseado antes de restaurar:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_imagen</span>`.dmg --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/volumen</span>` --erase`

- Omite la verificación después de restaurar:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_imagen</span>`.dmg --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/volumen</span>` --noverify`

- Clona volúmenes sin el uso de una imagen de disco intermedia:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/volumen</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/volumen_clonado</span>
