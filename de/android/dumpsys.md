---
layout: page
title: android/dumpsys (Deutsch)
description: "Stelle Informationen über Android-Systemservices bereit."
content_hash: a051c3a9ee65614319d3ff530802cf4ed26fb22e
related_topics:
  - title: English version
    url: /en/android/dumpsys.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/dumpsys.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/dumpsys.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/android/dumpsys.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/dumpsys.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/dumpsys.html
    icon: bi bi-globe
---
# dumpsys

Stelle Informationen über Android-Systemservices bereit.
Dieser Befehl kann nur mit `adb shell` verwendet werden.
Weitere Informationen: <https://developer.android.com/studio/command-line/dumpsys>.

- Erhalte diagnostische Informationen über alle Systemservices:

`dumpsys`

- Erhalte diagnostische Informationen über einen bestimmten Systemservice:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>

- Liste alle Services, über die `dumpsys` Informationen bereitstellen kann auf:

`dumpsys -l`

- Liste Service-spezifische Argumente für einen Service auf:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>` -h`

- Schließe einen bestimmten Service von den diagnostischen Informationen aus:

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>

- Gib ein Timeout in Sekunden an (standardmäßig 10s):

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sekunden</span>
