---
layout: page
title: linux/qmake (español)
description: "Genera Makefiles a partir de archivos de proyecto Qt."
content_hash: 99ea06ea98a41a01d4f39ca47d1c94238ae9301d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/qmake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qmake

Genera Makefiles a partir de archivos de proyecto Qt.
Más información: <https://doc.qt.io/qt-6/qmake-manual.html>.

- Genera un `Makefile` a partir de un archivo de proyecto en el directorio actual:

`qmake`

- Especifica la ubicación del `Makefile` y del archivo de proyecto:

`qmake -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/Makefile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_proyecto.pro</span>

- Genera un archivo de proyecto por defecto:

`qmake -project`

- Compila un proyecto:

`qmake && make`

- Activa el modo de depuración:

`qmake -d`
