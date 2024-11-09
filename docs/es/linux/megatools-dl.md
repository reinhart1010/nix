---
layout: page
title: linux/megatools-dl (español)
description: "Descarga archivos de `mega.nz`."
content_hash: 31d81c61beba50a7fcbb3d9dd9bbddd3c6f54ee4
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/megatools-dl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/megatools-dl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/megatools-dl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/megatools-dl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># megatools-dl

Descarga archivos de `mega.nz`.
Parte del paquete de utilidades `megatools`.
Más información: <https://megatools.megous.com/man/megatools-dl.html>.

- Descarga los archivos de un enlace 'mega.nz' al directorio actual:

`megatools-dl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://mega.nz/...</span>

- Descarga los archivos de un enlace 'mega.nz` a un directorio específico:

`megatools-dl --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://mega.nz/...</span>

- Permite elegir interactivamente qué archivos descargar:

`megatools-dl --choose-files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://mega.nz/...</span>

- Limita la velocidad de descarga en KiB/s:

`megatools-dl --limit-speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">velocidad</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://mega.nz/...</span>
