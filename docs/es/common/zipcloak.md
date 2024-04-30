---
layout: page
title: common/zipcloak (español)
description: "Encripta el contenido de un archivo zip."
content_hash: 95641f03d5dea3d273147ab84a6e814ddb9157aa
last_modified_at: 2024-04-30
related_topics:
  - title: English version
    url: /en/common/zipcloak.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zipcloak.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zipcloak

Encripta el contenido de un archivo zip.
Más información: <https://manned.org/zipcloak>.

- Encripta el contenido de un archivo zip:

`zipcloak `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.zip</span>

- [d]esencripta el contenido de un archivo zip:

`zipcloak -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_encriptado.zip</span>

- Genera un nuev[O] archivo zip con el contenido encriptado:

`zipcloak `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.zip</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_encriptado.zip</span>
