---
layout: page
title: common/apkleaks (español)
description: "Expone URIs, endpoints y secretos de archivos APK."
content_hash: ecb5a15e0186fada813a662666604c3dd63489cf
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/common/apkleaks.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/apkleaks.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/apkleaks.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/apkleaks.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apkleaks

Expone URIs, endpoints y secretos de archivos APK.
Nota: APKLeaks utiliza el desensamblador `jadx` para decompilar archivos APK.
Más información: <https://github.com/dwisiswant0/apkleaks>.

- Escanea un archivo APK en busca de URIs, endpoints y secretos:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.apk</span>

- Escanea y guarda el resultad[o] en un archivo específico:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.txt</span>

- Pasar [a]rgumentos del desensamblador `jadx`:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.apk</span>` --args "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--threads-count 5 --deobf</span>`"`
