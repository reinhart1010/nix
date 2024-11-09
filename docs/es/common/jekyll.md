---
layout: page
title: common/jekyll (español)
description: "Un generador de sitios estático sencillo que tiene en cuenta los blogs."
content_hash: ed1eb3924b2427fead425117c884d8746f39992d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/jekyll.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/jekyll.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jekyll.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/jekyll.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jekyll.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jekyll

Un generador de sitios estático sencillo que tiene en cuenta los blogs.
Más información: <https://jekyllrb.com/docs/usage/>.

- Genera un servidor de desarrollo que funcionará en http://localhost:4000/:

`jekyll serve`

- Habilita la regeneración incremental:

`jekyll serve --incremental`

- Habilita salida (output) detallada:

`jekyll serve --verbose`

- Genera el directorio actual en `./_site`:

`jekyll build`

- Limpia el sitio (site) (elimina el sitio generado y el directorio `cache`) sin construirlo:

`jekyll clean`
