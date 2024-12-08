---
layout: page
title: linux/farge (español)
description: "Muestra el color de un píxel específico de la pantalla en formatos hexadecimal o RGB."
content_hash: bc51cccede86a343bd8b8b97a3045ef4ec77232a
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/linux/farge.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/farge.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/farge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># farge

Muestra el color de un píxel específico de la pantalla en formatos hexadecimal o RGB.
Más información: <https://github.com/sdushantha/farge>.

- Muestra una pequeña ventana de vista previa del color de un píxel con su valor hexadecimal, y copia este valor al portapapeles:

`farge`

- Copia el valor hexadecimal de un píxel al portapapeles sin mostrar una ventana de vista previa:

`farge --no-preview`

- Envía el valor hexadecimal de un píxel a `stdout` y copia este valor al portapapeles:

`farge --stdout`

- Envía el valor RGB de un píxel a `stdout` y copia este valor al portapapeles:

`farge --rgb --stdout`

- Muestra el valor hexadecimal de un píxel como notificación que expira en 5000 milisegundos y copia este valor al portapapeles:

`farge --notify --expire-time 5000`
