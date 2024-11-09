---
layout: page
title: common/ranger (español)
description: "Gestor de archivos en consola con atajos de teclado de VI."
content_hash: 5cfd153ff88473d4b4e9895c00b06a14734dcc45
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/ranger.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ranger.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ranger.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ranger.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ranger

Gestor de archivos en consola con atajos de teclado de VI.
Vea también: `clifm`, `vifm`, `mc`, `dolphin`.
Más información: <https://github.com/ranger/ranger>.

- Abre Ranger:

`ranger`

- Muestra sólo directorios:

`ranger --show-only-dirs`

- Cambia el directorio de configuración:

`ranger --confdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Cambia el directorio de datos:

`ranger --datadir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Imprime estadísticas de uso de la CPU al salir:

`ranger --profile`
