---
layout: page
title: common/adb-shell (Nederlands)
description: "Android Debug Bridge Shell: Voer externe shell-opdrachten uit op een Android-emulatorinstantie of aangesloten Android-apparaten."
content_hash: e39e612727f2542d8783c48cb10078acf0ab0fe1
last_modified_at: 2024-02-22
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
  - title: italiano version
    url: /it/common/adb-shell.html
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

Android Debug Bridge Shell: Voer externe shell-opdrachten uit op een Android-emulatorinstantie of aangesloten Android-apparaten.
Meer informatie: <https://developer.android.com/tools/adb>.

- Start een externe interactieve shell op de emulator of het apparaat:

`adb shell`

- Haal alle eigenschappen op van de emulator of het apparaat:

`adb shell getprop`

- Zet alle runtime-machtigingen terug naar hun standaard:

`adb shell pm reset-permissions`

- Een gevaarlijke machtiging voor een toepassing intrekken:

`adb shell pm revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toestemming</span>

- Activeer een sleutelgebeurtenis:

`adb shell input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sleutelcode</span>

- Wis de gegevens van een applicatie op een emulator of apparaat:

`adb shell pm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Start een activiteit op emulator of apparaat:

`adb shell am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">activiteit</span>

- Start de thuisactiviteit op een emulator of apparaat:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
