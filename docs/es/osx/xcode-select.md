---
layout: page
title: osx/xcode-select (español)
description: "Cambia entre diferentes versiones de Xcode y las herramientas incluidas para desarrolladores."
content_hash: ba978bea349d85719a4554e8bcf69dac7033bbae
last_modified_at: 2023-08-09
related_topics:
  - title: Deutsch version
    url: /de/osx/xcode-select.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/xcode-select.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xcode-select

Cambia entre diferentes versiones de Xcode y las herramientas incluidas para desarrolladores.
También se utiliza para actualizar la ruta a Xcode si se mueve después de la instalación.
Más información: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Instala las herramientas de línea de comandos de Xcode:

`xcode-select --install`

- Selecciona una ruta determinada como directorio de desarrollador activo:

`xcode-select --switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/Xcode.app/Contents/Developer</span>

- Selecciona una instancia de Xcode determinada y utiliza su directorio de desarrollador como directorio activo:

`xcode-select --switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo/Xcode_file.app</span>

- Muestra el directorio de desarrollador seleccionado:

`xcode-select --print-path`

- Descarta cualquier directorio de desarrolladores especificado por el usuario para que se encuentre mediante el mecanismo de búsqueda predeterminado:

`sudo xcode-select --reset`
