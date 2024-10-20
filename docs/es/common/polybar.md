---
layout: page
title: common/polybar (español)
description: "Una barra de estado rápida y fácil de usar."
content_hash: 6165aefd5656fc6c9cb3d9a116acbb1657d3a3a6
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/polybar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/polybar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># polybar

Una barra de estado rápida y fácil de usar.
Más información: <https://github.com/polybar/polybar/wiki>.

- Inicia Polybar (el nombre de la barra es opcional si solo se ha definido una barra en la configuración):

`polybar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_barra</span>

- Inicia Polybar con la configuración especificada:

`polybar --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/config.ini</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_barra</span>

- Inicia Polybar y recarga la barra cuando se modifica el archivo de configuración:

`polybar --reload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_barra</span>
