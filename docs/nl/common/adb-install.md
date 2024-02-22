---
layout: page
title: common/adb-install (Nederlands)
description: "Android Debug Bridge-installatie: push pakketten naar een Android-emulatorinstantie of aangesloten Android-apparaten."
content_hash: 31960f6c63f87454fc672731423ec57004815685
last_modified_at: 2024-02-22
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
  - title: polski version
    url: /pl/common/adb-install.html
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
tldri18n_status: 2
---
# adb install

Android Debug Bridge-installatie: push pakketten naar een Android-emulatorinstantie of aangesloten Android-apparaten.
Meer informatie: <https://developer.android.com/tools/adb>.

- Push een Android-applicatie naar een emulator/apparaat:

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.apk</span>

- Een Android-applicatie naar een specifieke emulator/apparaat pushen (heeft voorrang op `$ANDROID_SERIAL`):

`adb -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">serienummer</span>` install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.apk</span>

- Installeer een bestaande app opnieuw, waarbij de gegevens behouden blijven:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.apk</span>

- Een Android-applicatie pushen die downgrade van versiecode mogelijk maakt (alleen foutopsporingspakketten):

`adb install -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.apk</span>

- Verleen alle machtigingen die worden vermeld in het app-manifest:

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.apk</span>

- Werk snel een geïnstalleerd pakket bij door alleen de delen van de APK bij te werken die zijn gewijzigd:

`adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.apk</span>
