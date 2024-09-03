---
layout: page
title: android/pm (polski)
description: "Pokaż informacje o aplikacjach na urządzeniu z systemem Android."
content_hash: b09922f70223b1badb824fe89a58f4b27a35d8fb
last_modified_at: 2024-09-03
related_topics:
  - title: বাংলা version
    url: /bn/android/pm.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/pm.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/pm.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/pm.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/android/pm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/pm.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/android/pm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/pm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/android/pm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/pm.html
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
  - title: українська version
    url: /uk/android/pm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/pm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/pm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pm

Pokaż informacje o aplikacjach na urządzeniu z systemem Android.
Więcej informacji: <https://developer.android.com/tools/adb#pm>.

- Wypisz wszystkie zainstalowane aplikacje:

`pm list packages`

- Wypisz wszystkie zainstalowane aplikacje [s]ystemowe:

`pm list packages -s`

- Wypisz wszystkie zainstalowane aplikacje firm trzecich ([3]):

`pm list packages -3`

- Wypisz aplikacje pasujące do określonych słów kluczowych:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">słowo_kluczowe1 słowo_kluczowe2 ...</span>

- Pokaż ścieżkę APK konkretnej aplikacji:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplikacja</span>
