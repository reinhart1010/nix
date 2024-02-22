---
layout: page
title: common/adb-install (italiano)
description: "Android Debug Bridge Install: Invia pacchetti ad un emulatore Android od ad un dispositivo Android connesso."
content_hash: e0515bee38a3d2e4587f16d13bcd7092431c93a4
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
  - title: Nederlands version
    url: /nl/common/adb-install.html
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adb install

Android Debug Bridge Install: Invia pacchetti ad un emulatore Android od ad un dispositivo Android connesso.
Maggiori informazioni: <https://developer.android.com/tools/adb>.

- Invia un'applicazione Android ad un emulatore emulatore/Android:

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.apk</span>

- Reinstalla una applicazione esistente, preservandone i dati:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.apk</span>

- Fornisce tutti i permessi elencati nel manifest dell'applicazione:

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.apk</span>

- Aggiorna rapidamente un pacchetto installato aggiornando solamente le parti dell'APK che sono cambiate:

`adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.apk</span>
