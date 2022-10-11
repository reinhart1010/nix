---
layout: page
title: android/pm (polski)
description: "Pokaż informacje o aplikacjach na urządzeniu z systemem Android."
content_hash: 343b39c89240296dd11eeafa54b3b2e64dfa2a02
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

Pokaż informacje o aplikacjach na urządzeniu z systemem Android.
Więcej informacji: <https://developer.android.com/studio/command-line/adb#pm>.

- Listuj wszystkie zainstalowane aplikacje:

`pm list packages`

- Listuj wszystkie zainstalowane aplikacje systemowych:

`pm list packages -s`

- Listuj wszystkie zainstalowane aplikacje firm trzecich

`pm list packages -3`

- Listuj aplikacje pasujące do określonych słów kluczowych:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">słowo_kluczowe</span>

- Pokaż ścieżkę APK konkretnej aplikacji:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplikacja</span>
