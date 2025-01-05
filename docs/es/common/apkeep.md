---
layout: page
title: common/apkeep (español)
description: "Descarga archivos APK de varias fuentes."
content_hash: 78702cf722a61cc42250b70845540d1915063988
last_modified_at: 2025-01-05
related_topics:
  - title: English version
    url: /en/common/apkeep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apkeep

Descarga archivos APK de varias fuentes.
Más información: <https://github.com/EFForg/apkeep>.

- Descarga un archivo APK al directorio especificado:

`apkeep --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.application</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Lista todas las versiones disponibles para descarga:

`apkeep --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.application</span>` --list-versions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Especifica la tienda para hacer la descarga:

`apkeep --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.application</span>` --download-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apk-pure|google-play|f-droid|huawei-app-gallery</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>
