---
layout: page
title: common/pambrighten (español)
description: "Cambia la saturación y el valor de una imagen PAM."
content_hash: f69bfd1f6406f90da033a0443194a8ece1e32470
last_modified_at: 2024-05-13
related_topics:
  - title: English version
    url: /en/common/pambrighten.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pambrighten.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pambrighten

Cambia la saturación y el valor de una imagen PAM.
Más información: <https://netpbm.sourceforge.net/doc/pambrighten.html>.

- Aumenta la saturación de cada píxel con un porcentaje específico:

`pambrighten -saturation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_porcentual</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_de_salida.pam</span>

- Aumenta el valor (del espacio de color HSV) de cada píxel con un porcentaje específico:

`pambrighten -value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_porcentual</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_de_salida.pam</span>
