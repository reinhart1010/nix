---
layout: page
title: common/adb-shell (polski)
description: "Android Debug Bridge Shell: uruchamiaj zdalne polecenia powłoki na instancji emulatora Androida lub podłączonych urządzeniach z Androidem."
content_hash: 7bda118883be2dedddc4d0baaed1e559beedca11
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
  - title: italiano version
    url: /it/common/adb-shell.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-shell.html
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

Android Debug Bridge Shell: uruchamiaj zdalne polecenia powłoki na instancji emulatora Androida lub podłączonych urządzeniach z Androidem.
Więcej informacji: <https://developer.android.com/studio/command-line/adb>.

- Uruchom interaktywną zdalną powłokę na emulatorze / urządzeniu:

`adb shell`

- Pobierz wszystkie właściwości z emulatora lub urządzenia:

`adb shell getprop`

- Przywróć wszystkie uprawnienia wykonawcze do ich wartości domyślnych:

`adb shell pm reset-permissions`

- Odwołaj niebezpieczne pozwolenie dla aplikacji:

`adb shell pm revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paczka</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pozwolenie</span>

- Wywołaj zdarzenie klawisza:

`adb shell input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kod_klucza</span>

- Wyczyść dane aplikacji na emulatorze lub urządzeniu:

`adb shell pm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paczka</span>

- Rozpocznij aktywność na emulatorze / urządzeniu:

`adb shell am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paczka</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aktywność</span>

- Rozpocznij aktywność domową na emulatorze lub urządzeniu:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
