---
layout: page
title: common/aapt (Nederlands)
description: "Android Asset Packaging-tool."
content_hash: bc6d5b8d0ad126a8a35b5fc39858b87fd645a882
last_modified_at: 2023-11-04
related_topics:
  - title: বাংলা version
    url: /bn/common/aapt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/aapt.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aapt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aapt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aapt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/aapt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aapt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aapt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aapt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/aapt.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aapt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aapt.html
    icon: bi bi-globe
---
# aapt

Android Asset Packaging-tool.
Compileer en verpak de bronnen van een Android-app.
Meer Informatie: <https://elinux.org/Android_aapt>.

- Maak een lijst van bestanden in een APK-archief:

`aapt list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/app.apk</span>

- Geef de metadata van een app weer (versie, machtigingen, enz.):

`aapt dump badging `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/app.apk</span>

- Maak een nieuw APK-archief met bestanden uit de opgegeven map:

`aapt package -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/app.apk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>
