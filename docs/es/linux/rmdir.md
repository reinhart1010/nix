---
layout: page
title: linux/rmdir (español)
description: "Elimina directorios sin archivos."
content_hash: 7bbda1f563d8834d5af067c073c15c61b841d183
last_modified_at: 2024-12-19
related_topics:
  - title: English version
    url: /en/linux/rmdir.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/rmdir.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/rmdir.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/rmdir.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rmdir.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rmdir

Elimina directorios sin archivos.
Vea también: `rm`.
Más información: <https://www.gnu.org/software/coreutils/rmdir>.

- Elimina directorios específicos:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio1 ruta/al/directorio2 ...</span>

- Elimina directorios específicos anidados recursivamente:

`rmdir --parents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio1 ruta/al/directorio2 ...</span>
