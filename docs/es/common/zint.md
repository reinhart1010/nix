---
layout: page
title: common/zint (español)
description: "Genera códigos de barras y códigos QR."
content_hash: af71653be906fc626bd5d09bd20c9fca5764b373
last_modified_at: 2024-07-01
related_topics:
  - title: English version
    url: /en/common/zint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zint

Genera códigos de barras y códigos QR.
Más información: <https://www.zint.org.uk/manual/chapter/4>.

- Crea un archivo con un código de barras:

`zint --data "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datos_UTF-8</span>`" --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Crea un archivo con otro tipo de código de barras:

`zint --barcode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_de_código</span>` --data "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datos_UTF-8</span>`" --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Lista todos los tipos de códigos de barras soportados:

`zint --types`
