---
layout: page
title: common/adb-reverse (Nederlands)
description: "Android Debug Bridge Reverse: omgekeerde socketverbindingen van een Android-emulatorinstantie of verbonden Android-apparaten."
content_hash: 01841c580acf9196d3b3426c4a9a3a31ea00ca0f
last_modified_at: 2023-06-01
related_topics:
  - title: English version
    url: /en/common/adb-reverse.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-reverse.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-reverse.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-reverse.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-reverse.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-reverse.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-reverse.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adb reverse

Android Debug Bridge Reverse: omgekeerde socketverbindingen van een Android-emulatorinstantie of verbonden Android-apparaten.
Meer informatie: <https://developer.android.com/studio/command-line/adb>.

- Maak een lijst van alle omgekeerde socketverbindingen van emulators en apparaten:

`adb reverse --list`

- Keer een TCP-poort om van een emulator of apparaat naar localhost:

`adb reverse tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">externe_poort</span>` tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokale_poort</span>

- Verwijder omgekeerde socketverbindingen van een emulator of apparaat:

`adb reverse --remove tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">externe_poort</span>

- Verwijder alle omgekeerde socketverbindingen van alle emulators en apparaten:

`adb reverse --remove-all`
