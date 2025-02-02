---
layout: page
title: common/adb (polski)
description: "Android Debug Bridge: komunikuj się z instancją emulatora Androida lub podłączonym urządzeniem z Androidem."
content_hash: ebf360fe0ffc7de47a6414f1cd88718a1a2ced3a
last_modified_at: 2024-12-27
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adb

Android Debug Bridge: komunikuj się z instancją emulatora Androida lub podłączonym urządzeniem z Androidem.
Niektóre podkomendy takie jak `shell` mają osobną dokumentację.
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
