---
layout: page
title: common/zola (español)
description: "Un generador de sitios estáticos en un único binario con todo incorporado."
content_hash: c9b88bda75c20cd6d4f093b4132bbc816e00feda
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/common/zola.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zola.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zola.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zola.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zola.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zola

Un generador de sitios estáticos en un único binario con todo incorporado.
Más información: <https://www.getzola.org/documentation/getting-started/cli-usage/>.

- Crea la estructura de directorios utilizada por Zola en el directorio dado:

`zola init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mi_sitio</span>

- Construye todo el sitio en el directorio `public` después de eliminarlo:

`zola build`

- Construye todo el sitio en un directorio diferente:

`zola build --output-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio_resultado/</span>

- Construye y sirve el sitio usando un servidor local (por defecto es `127.0.0.1:1111`):

`zola serve`

- Construye todas las páginas como lo haría el comando build, pero sin escribir ninguno de los resultados al disco:

`zola check`
