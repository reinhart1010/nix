---
layout: page
title: common/pamtouil (español)
description: "Convierte un archivo PNM o PAM en un archivo de iconos UIL de Motif."
content_hash: 66856f4e22d8d98a1879a1d9d47c3bf903cfb8eb
last_modified_at: 2024-04-22
related_topics:
  - title: English version
    url: /en/common/pamtouil.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamtouil.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamtouil

Convierte un archivo PNM o PAM en un archivo de iconos UIL de Motif.
Más información: <https://netpbm.sourceforge.net/doc/pamtouil.html>.

- Convierte un archivo PNM o PAM en un archivo de icono Motif UIL:

`pamtouil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/entrada.[pnm|pam]</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.uil</span>

- Especifique una cadena de prefijo que se imprimirá en el archivo UIL de salida:

`pamtouil -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_uil</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/entrada.[pnm|pam]</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.uil</span>
