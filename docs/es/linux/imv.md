---
layout: page
title: linux/imv (español)
description: "Visor de imágenes de línea de comando para Wayland y X11 dirigido a gestores de ventanas en mosaico."
content_hash: 523f4f2326d32da3044485f87393cacd893e319b
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/linux/imv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/imv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># imv

Visor de imágenes de línea de comando para Wayland y X11 dirigido a gestores de ventanas en mosaico.
Maneja múltiples formatos incluyendo Photoshop (PSD).
Más información: <https://sr.ht/~exec64/imv>.

- Muestra múltiples imágenes:

`imv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen1.ext ruta/a/la/imagen2.ext ...</span>

- Vista en modo de pantalla completa:

`imv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.ext</span>

- Muestra imágenes de un directorio [r]ecursivamente:

`imv -r --slideshow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Abre múltiples imágenes vía `stdin`:

`find . -type f -name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.svg</span>`" | imv`

- Hace una presentación desde un directorio que muestra cada imagen durante 10 segundos:

`imv -t 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Muestra múltiples imágenes de la web:

`curl -Osw '%{filename_effective}\n' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.example.com/[1-10].jpg</span>`' | imv`
