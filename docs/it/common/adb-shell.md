---
layout: page
title: common/adb-shell (italiano)
description: "Android Debug Bridge Shell: Esegue un commando remoto sull'emulatore o dispositivo Android connesso."
content_hash: fbe16f76eaea8a2112be16d3709ef78f23d311b5
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/adb-shell.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-shell.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-shell.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/adb-shell.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-shell.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-shell.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-shell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-shell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-shell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-shell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb shell

Android Debug Bridge Shell: Esegue un commando remoto sull'emulatore o dispositivo Android connesso.
Maggiori informazioni: <https://developer.android.com/studio/command-line/adb>.

- Avvia un interprete di comandi iterativo remoto sull'emulatore/dispositivo:

`adb shell`

- Fornisce tutte le proprietà dell'emulatore o dispositivo:

`adb shell getprop`

- Ripristina tutti i permessi di esecuzione ai loro valori predefiniti:

`adb shell pm reset-permissions`

- Revoca un permesso pericoloso da un'applicazione:

`adb shell pm revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">permesso</span>

- Attiva un evento chiave:

`adb shell input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keycode</span>

- Pulisce i dati di un'applicazione sull'emulatore o dispositivo:

`adb shell pm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Avvia un'attività sull'emulatore/dispositivo:

`adb shell am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attività</span>

- Avvia la schermata iniziale sull'emulatore o dispositivo:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
