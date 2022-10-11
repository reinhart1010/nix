---
layout: page
title: android/pm (português (Portugal))
description: "Mostra informações sobre aplicações num dispositivo Android."
content_hash: 4e5f9fc490f546349b890bdf31abdd1e8344416c
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
  - title: português (Brasil) version
    url: /pt_BR/android/pm.html
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

Mostra informações sobre aplicações num dispositivo Android.
Mais informações: <https://developer.android.com/studio/command-line/adb#pm>.

- Exibir uma lista com todas as aplicações instaladas:

`pm list packages`

- Exibir uma lista com todas as aplicações do sistema instaladas:

`pm list packages -s`

- Exibir uma lista todas as aplicações de terceiros instaladas:

`pm list packages -3`

- Exibir uma lista com todas as aplicações cujos nomes estejam incluídos em palavras-chave:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavras_chave</span>

- Exibir o caminho para o APK de um app:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app</span>
