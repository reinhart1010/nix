---
layout: page
title: common/adb (polski)
description: "Android Debug Bridge: komunikuj się z instancją emulatora Androida lub podłączonym urządzeniem z Androidem."
content_hash: 22a0ccac0beba7a4dbbd06c9ef2044c995cf9fab
last_modified_at: 2023-11-12
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
Więcej informacji: <https://developer.android.com/studio/command-line/adb>.

- Sprawdź czy proces serwera adb działa, jeśli nie, uruchom go:

`adb start-server`

- Zakończ proces serwera adb:

`adb kill-server`

- Uruchom powłokę w instancji emulatora lub urządzeniu:

`adb shell`

- Wypchnij aplikację Androidową do instancji emulatora lub urządzenia:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.apk</span>

- Skopiuj plik/katalog do urządzenia:

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu_na_urządzeniu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/lokalnego_katalogu</span>

- Skopiuj plik/katalog z urządzenia:

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu_na_urządzeniu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/lokalnego_katalogu</span>

- Listuj połączone lub emulowane urządzenia:

`adb devices`
