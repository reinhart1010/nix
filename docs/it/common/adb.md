---
layout: page
title: common/adb (italiano)
description: "Android Debug Bridge: comunica con un'instanza di un emulatore Android o con un dispositivo android connesso."
content_hash: 0b25d7d96ca85b3385b7f9fa79377eda6748fa1b
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
  - title: 한국어 version
    url: /ko/common/adb.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb.html
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

Android Debug Bridge: comunica con un'instanza di un emulatore Android o con un dispositivo android connesso.
Alcuni comandi aggiuntivi, come `shell`, hanno la propria documentazione.
Maggiori informazioni: <https://developer.android.com/tools/adb>.

- Controlla se il processo server adb è attivo ed avvialo:

`adb start-server`

- Termina il processo server adb:

`adb kill-server`

- Avvia una shell remota nell'emulatore o dispositivo target:

`adb shell`

- Installa un'applicazione Android nell'emulatore o dispositivo target:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.apk</span>

- Copia file o directory dal dispositivo target:

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory_dispositivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory_locale</span>

- Copia file/directory sul dispositivo target:

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory_locale</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_destinazione_dispositivo</span>

- Mostra una lista dei dispositivi connessi:

`adb devices`
