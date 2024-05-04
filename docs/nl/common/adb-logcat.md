---
layout: page
title: common/adb-logcat (Nederlands)
description: "Dump een logboek met systeemberichten."
content_hash: 9dfddd0505e1b38dbceb7828ccb4c8e4d0cd78cc
last_modified_at: 2024-05-04
related_topics:
  - title: English version
    url: /en/common/adb-logcat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-logcat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-logcat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb logcat

Dump een logboek met systeemberichten.
Meer informatie: <https://developer.android.com/tools/logcat>.

- Geef systeemlogboeken weer:

`adb logcat`

- Geef regels weer die overeenkomen met een reguliere expressie:

`adb logcat -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>

- Toon logs voor een tag in een specifieke modus ([V]erbose, [D]ebug, [I]nfo, [W]arning, [E]rror, [F]atal, [S]ilent), andere tags filteren:

`adb logcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modus</span>` *:S`

- Geef logs weer voor React Native-applicaties in [V]erbose mode [S]ilencing andere tags:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Toon logboeken voor alle tags met prioriteitsniveau [W]arning en hoger:

`adb logcat *:W`

- Geef logboeken weer voor een specifiek proces:

`adb logcat --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Logboeken weergeven voor het proces van een specifiek pakket:

`adb logcat --pid $(adb shell pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>`)`

- Kleur de log in (gebruik meestal met filters):

`adb logcat -v color`
