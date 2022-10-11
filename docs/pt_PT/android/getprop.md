---
layout: page
title: android/getprop (português (Portugal))
description: "Obtém informações sobre propriedades do sistema (system props) Android."
content_hash: 2e02bf49307a53da6740924327e29fe69bc03290
related_topics:
  - title: Deutsch version
    url: /de/android/getprop.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/getprop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/getprop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/getprop.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/getprop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/getprop.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/getprop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/getprop.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/getprop.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># getprop

Obtém informações sobre propriedades do sistema (system props) Android.
Mais informações: <https://manned.org/getprop>.

- Mostrar todas as propriedades do sistema:

`getprop`

- Mostrar o valor de uma propriedade específica:

`getprop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prop</span>

- Mostrar o nível de API:

`getprop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ro.build.version.sdk</span>

- Mostrar a versão do Android:

`getprop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ro.build.version.release</span>

- Mostrar o modelo do dispositivo:

`getprop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ro.vendor.product.model</span>

- Mostrar o status de desbloqueio OEM:

`getprop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ro.oem_unlock_supported</span>

- Mostrar o endereço MAC da placa de Wi-Fi do dispositivo:

`getprop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ro.boot.wifimacaddr</span>
