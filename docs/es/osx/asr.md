---
layout: page
title: osx/asr (español)
description: "Restaura (copia) una imagen de disco en un volumen."
content_hash: c94c6d173a2fd154a18d75d597050a937c437e31
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/asr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/asr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/asr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/asr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asr

Restaura (copia) una imagen de disco en un volumen.
El nombre del comando significa Restauración de Software de Apple.
Más información: <https://keith.github.io/xcode-man-pages/asr.8.html>.

- Restaura una imagen de disco en un volumen:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_imagen.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/volumen</span>

- Borra el volumen deseado antes de restaurar:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_imagen.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/volumen</span>` --erase`

- Omite la verificación después de restaurar:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_imagen.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/volumen</span>` --noverify`

- Clona volúmenes sin el uso de una imagen de disco intermedia:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/volumen</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/volumen_clonado</span>
