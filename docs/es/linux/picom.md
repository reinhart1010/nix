---
layout: page
title: linux/picom (español)
description: "Compositor independiente para Xorg."
content_hash: cb23997e5e1f69e5e53802410168d84ddfc52a33
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/linux/picom.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/picom.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># picom

Compositor independiente para Xorg.
Más información: <https://manned.org/picom>.

- Habilita `picom` durante una sesión:

`picom &`

- Inicia `picom` como proceso en segundo plano:

`picom -b`

- Utiliza un archivo de configuración personalizado:

`picom --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_configuración</span>
