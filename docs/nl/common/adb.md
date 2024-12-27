---
layout: page
title: common/adb (Nederlands)
description: "Android Debug-Brug: communiceer met een Android-emulator of een aangesloten Android-apparaat."
content_hash: bf56709ab8dc9de85cba3dbb3b2f88d6d16c63f2
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

Android Debug-Brug: communiceer met een Android-emulator of een aangesloten Android-apparaat.
Sommige subcommando's zoals `shell` hebben hun eigen documentatie.
Meer informatie: <https://developer.android.com/tools/adb>.

- Controleer of het adb serverproces draait en start het:

`adb start-server`

- Sluit het adb serverproces:

`adb kill-server`

- Start een afstandshell voor de doelemulator of apparaatinstantie:

`adb shell`

- Stuur een Android-applicatie naar de emulator/het apparaat:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.apk</span>

- Kopiëer een bestand/map van het doelapparaat:

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/extern/bestand_of_map</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/lokaal/bestand_of_map</span>

- Kopiëer een bestand/map naar het doelapparaat:

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/lokaal/bestand_of_map</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/extern/bestand_of_map</span>

- Krijg een lijst met aangesloten apparaten:

`adb devices`
