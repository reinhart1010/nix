---
layout: page
title: common/pamflip (español)
description: "Refleja o gira una imagen PAM o PNM."
content_hash: 2f0d2ed0c363c9280fa4d333d3ab5e001bc3b8b5
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/common/pamflip.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pamflip.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamflip.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamflip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamflip

Refleja o gira una imagen PAM o PNM.
Más información: <https://netpbm.sourceforge.net/doc/pamflip.html>.

- Gira la imagen de entrada en sentido contrario a las manecillas del reloj una cantidad de grados específica:

`pamflip -rotate`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90|180|270</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pam</span>

- Refleja horizontalmente:

`pamflip -leftright `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pam</span>

- Refleja verticalmente:

`pamflip -topbottom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pam</span>

- Refleja la imagen de entrada por la diagonal principal:

`pamflip -transpose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pam</span>
