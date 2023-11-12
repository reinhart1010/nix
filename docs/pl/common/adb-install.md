---
layout: page
title: common/adb-install (polski)
description: "Android Debug Bridge Install: wysyłaj pakiety do instancji emulatora Androida lub podłączonych urządzeń z systemem Android."
content_hash: ab65ed6ab41bb95283cdfba43d73ec753e3c77b5
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/adb-install.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-install.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-install.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-install.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-install.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adb install

Android Debug Bridge Install: wysyłaj pakiety do instancji emulatora Androida lub podłączonych urządzeń z systemem Android.
Więcej informacji: <https://developer.android.com/studio/command-line/adb>.

- Wyślij aplikację na Androida do emulatora / urządzenia:

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scieżka/do/pliku.apk</span>

- Zainstaluj ponownie istniejącą aplikację, zachowując jej dane:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scieżka/do/pliku.apk</span>

- Przyznaj wszystkie uprawnienia wymienione w pliku manifestu aplikacji:

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scieżka/do/pliku.apk</span>

- Szybko zaktualizuj zainstalowany pakiet, aktualizując tylko te części APK, które się zmieniły:

`adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scieżka/do/pliku.apk</span>
