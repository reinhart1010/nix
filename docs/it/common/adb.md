---
layout: page
title: common/adb (italiano)
description: "Android Debug Bridge: comunica con un'instanza di un emulatore Android o con un dispositivo android connesso."
content_hash: dc04e25dc6c1fa22e30e354a329e53ce400fcadd
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
---
# adb

Android Debug Bridge: comunica con un'instanza di un emulatore Android o con un dispositivo android connesso.
Alcuni comandi aggiuntivi, come `adb shell`, hanno la propria documentazione.
Maggiori informazioni: <https://developer.android.com/studio/command-line/adb>.

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
