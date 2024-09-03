---
layout: page
title: common/adb (polski)
description: "Android Debug Bridge: komunikuj się z instancją emulatora Androida lub podłączonym urządzeniem z Androidem."
content_hash: 671779ea0434ce6da423a3485bcde5f3bea5e7e2
last_modified_at: 2024-09-03
related_topics:
  - title: English version
    url: /en/common/adb.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/adb.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb

Android Debug Bridge: komunikuj się z instancją emulatora Androida lub podłączonym urządzeniem z Androidem.
Niektóre podkomendy takie jak `adb shell` mają osobną dokumentację.
Więcej informacji: <https://developer.android.com/tools/adb>.

- Sprawdź czy proces serwera adb działa, jeśli nie, uruchom go:

`adb start-server`

- Zakończ proces serwera adb:

`adb kill-server`

- Uruchom powłokę w docelowej instancji emulatora/urządzenia:

`adb shell`

- Wyślij aplikację Android do emulatora/urządzenia:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.apk</span>

- Skopiuj plik/katalog z urządzenia docelowego:

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu_na_urządzeniu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/lokalnego_katalogu_docelowego</span>

- Skopiuj plik/katalog do urządzenia docelowego:

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/lokalnego_pliku_lub_katalogu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/docelowego_katalogu_na_urządzeniu</span>

- Wypisz wszystkie połączone urządzenia:

`adb devices`
