---
layout: page
title: common/adb-reverse (polski)
description: "Android Debug Bridge Reverse: zwrotne połączenie socketowe z emulowanego lub prawdziwego urządzenia Android."
content_hash: abef47d970abee9b259ec5b454452fe96ebc5a97
last_modified_at: 2023-11-12
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
  - title: Nederlands version
    url: /nl/common/adb-reverse.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-reverse.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-reverse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb reverse

Android Debug Bridge Reverse: zwrotne połączenie socketowe z emulowanego lub prawdziwego urządzenia Android.
Więcej informacji: <https://developer.android.com/studio/command-line/adb>.

- Listuj wszystkie zwrotne połączenia socketowe z emulatorów i urządzeń:

`adb reverse --list`

- Przekieruj port TCP z emulatora lub urządzenia do localhost:

`adb reverse tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>` tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>

- Usuń wybrane zwrotne połączenie z emulatora lub urządzenia:

`adb reverse --remove tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>

- Usuń wszystkie zwrotne połączenie z emulatorów lub urządzeń:

`adb reverse --remove-all`
