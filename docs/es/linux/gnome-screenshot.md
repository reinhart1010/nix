---
layout: page
title: linux/gnome-screenshot (español)
description: "Captura la pantalla, una ventana o un área definida por el usuario y guarda la imagen a un archivo."
content_hash: 535bd06d034c18f44c8c49d5ef5f3d042799109f
last_modified_at: 2024-11-30
related_topics:
  - title: English version
    url: /en/linux/gnome-screenshot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/gnome-screenshot.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/gnome-screenshot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/gnome-screenshot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gnome-screenshot

Captura la pantalla, una ventana o un área definida por el usuario y guarda la imagen a un archivo.
Más información: <https://manned.org/gnome-screenshot>.

- Toma una captura de pantalla y la guarda en la ubicación predeterminada, normalmente `~/Pictures`:

`gnome-screenshot`

- Toma una captura de pantalla y la guarda en la ubicación de archivo indicada:

`gnome-screenshot --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Toma una captura de pantalla y la guarda en el portapapeles:

`gnome-screenshot --clipboard`

- Toma una captura después de un número determinado de segundos:

`gnome-screenshot --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Lanza la interfaz gráfica (GUI) de Captura de Pantalla GNOME:

`gnome-screenshot --interactive`

- Toma una captura de pantalla de la ventana actual y la guarda en la ubicación especificada:

`gnome-screenshot --window --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Toma una captura después del un número determinado de segundos y la guarda en el portapapeles:

`gnome-screenshot --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --clipboard`

- Muestra la versión:

`gnome-screenshot --version`
