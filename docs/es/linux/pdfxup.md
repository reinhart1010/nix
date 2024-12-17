---
layout: page
title: linux/pdfxup (español)
description: "N-up páginas PDF."
content_hash: f0ef80b1f656d061166e399b85496958a45cd95f
last_modified_at: 2024-12-17
related_topics:
  - title: English version
    url: /en/linux/pdfxup.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pdfxup.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pdfxup.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pdfxup

N-up páginas PDF.
N-upping significa poner múltiples páginas en una página escalando y rotándolas en una cuadrícula.
Más información: <https://ctan.org/pkg/pdfxup>.

- Crea un 2-up PDF:

`pdfxup -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.pdf</span>

- Crea un PDF con 3 columnas y 2 líneas por página:

`pdfxup -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.pdf</span>

- Crea un PDF en modo cuadernillo (2-up, y las páginas se ordenan para formar un libro cuando se doblan):

`pdfxup -b -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.pdf</span>
