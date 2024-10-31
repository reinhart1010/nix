---
layout: page
title: common/pnmnorm (español)
description: "Normaliza el contraste en una imagen PNM."
content_hash: 779adf790c34925bb505df1dc066226ed9325636
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/pnmnorm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pnmnorm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnmnorm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnmnorm

Normaliza el contraste en una imagen PNM.
Vea también: `pnmhisteq`.
Más información: <https://netpbm.sourceforge.net/doc/pnmnorm.html>.

- Fuerza los píxeles más brillantes a ser blancos, los más oscuros hacia negro y disemina los demás linealmente:

`pnmnorm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pnm</span>

- Fuerza los píxeles más brillantes a ser blancos, los más oscuros hacia negro y disemina los demás cuadráticamente, de tal forma que los píxeles con un brillo de 'n' tienen un 50 % del brillo:

`pnmnorm -midvalue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pnm</span>

- Mantiene el tono (hue) de los píxeles, solo modifica el brillo:

`pnmnorm -keephues `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pnm</span>

- Especifica un método para calcular el brillo de un píxel:

`pnmnorm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">luminosity|colorvalue|saturation</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pnm</span>
