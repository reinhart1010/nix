---
layout: page
title: linux/trash (español)
description: "Gestiona el contenedor de basura/reciclaje."
content_hash: 2f45ed17c695c0356ea995068c3c9e5678ad92ff
last_modified_at: 2024-11-30
related_topics:
  - title: English version
    url: /en/linux/trash.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/trash.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/trash.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/trash.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/trash.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># trash

Gestiona el contenedor de basura/reciclaje.
Más información: <https://github.com/andreafrancia/trash-cli>.

- Envía un archivo a la basura:

`trash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Lista todos los archivos en la basura:

`trash-list`

- Restaura interactivamente un archivo de la basura:

`trash-restore`

- Vacía la basura:

`trash-empty`

- Elimina permanentemente todos los archivos en la basura mayores a 10 días:

`trash-empty 10`

- Elimina todos los archivos en la basura, que coinciden con un patrón blob específico:

`trash-rm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.o</span>`"`

- Elimina todos los archivos con una ubicación original específica:

`trash-rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/al/archivo_o_directorio</span>
