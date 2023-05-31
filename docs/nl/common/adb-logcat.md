---
layout: page
title: common/adb-logcat (Nederlands)
description: "Dump een logboek met systeemberichten."
content_hash: c327b9389bb5c272c1b8d4946bc662378771f5d0
last_modified_at: 2023-05-31
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
  - title: 中文 version
    url: /zh/common/adb-logcat.html
    icon: bi bi-globe
---
# adb logcat

Dump een logboek met systeemberichten.
Meer informatie: <https://developer.android.com/studio/command-line/logcat>.

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

`adb logcat --pid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Logboeken weergeven voor het proces van een specifiek pakket:

`adb logcat --pid=$(adb shell pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>`)`

- Kleur de log in (gebruik meestal met filters):

`adb logcat -v color`
