---
layout: page
title: linux/swww (español)
description: "Servicio (daemon) eficiente de fondos de pantalla animados para Wayland."
content_hash: 8cc6b7a8cbd58ef0360d56def5f44c0d445d7480
last_modified_at: 2024-11-30
related_topics:
  - title: English version
    url: /en/linux/swww.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/swww.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/swww.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># swww

Servicio (daemon) eficiente de fondos de pantalla animados para Wayland.
Vea también: `swww-daemon`.
Más información: <https://github.com/LGFae/swww>.

- Establece fondo de pantalla:

`swww img `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen</span>

- Establece el fondo de pantalla en las salidas especificadas:

`swww img -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">salida1,salida2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen</span>

- Restaura el último fondo de pantalla:

`swww restore`

- Apaga daemon:

`swww kill`

- Muestra información de salida:

`swww query`
