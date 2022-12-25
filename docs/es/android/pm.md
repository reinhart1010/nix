---
layout: page
title: android/pm (español)
description: "Muestra información sobre aplicaciones en un dispositivo Android."
content_hash: a8140f87b35935c1164a13334d3d68d34d98a28d
last_modified_at: 2022-12-25
related_topics:
  - title: Deutsch version
    url: /de/android/pm.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/pm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/pm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/pm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/pm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/pm.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/pm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/pm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/pm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/pm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/pm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/pm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pm

Muestra información sobre aplicaciones en un dispositivo Android.
Más información: <https://developer.android.com/studio/command-line/adb#pm>.

- Genera una lista de todas las aplicaciones instaladas:

`pm list packages`

- Genera una lista de todas las aplicaciones del sistema instaladas:

`pm list packages -s`

- Genera una lista de todas las aplicaciones de terceros instaladas:

`pm list packages -3`

- Genera una lista de aplicaciones que coinciden con determinadas palabras clave:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabras_clave</span>

- Imprime la ruta del APK de una aplicación específica:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app</span>
