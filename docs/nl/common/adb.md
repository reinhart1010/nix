---
layout: page
title: common/adb (Nederlands)
description: "Android Debug-Brug: communiceer met een Android-emulator of een aangesloten Android-apparaat."
content_hash: c7771a3eaac2206091a0f91774c73c13601ee7cc
last_modified_at: 2025-01-04
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
tldri18n_status: 2
---
# adb

Android Debug-Brug: communiceer met een Android-emulator of een aangesloten Android-apparaat.
Sommige subcommando's zoals `shell` hebben hun eigen documentatie.
Meer informatie: <https://developer.android.com/tools/adb>.

- Controleer of het adb serverproces draait en start het:

`adb start-server`

- Sluit het adb serverproces:

`adb kill-server`

- Start een remote shell voor de doel-emulator of apparaat-instantie:

`adb shell`

- Stuur een Android-applicatie naar de emulator/het apparaat:

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.apk</span>

- Kopiëer een bestand/map van het doelapparaat:

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/extern/bestand_of_map</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/lokaal/bestand_of_map</span>

- Kopiëer een bestand/map naar het doelapparaat:

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/lokaal/bestand_of_map</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/extern/bestand_of_map</span>

- Toon alle aangesloten apparaten:

`adb devices`

- Specificeer naar welk apparaat de opdrachten verzonden dienen te worden als er meerdere apparaten zijn:

`adb -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apparaat_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell</span>
