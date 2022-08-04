---
layout: page
title: android/pm (Deutsch)
description: "Zeige Informationen über Apps auf einem Android Gerät."
content_hash: b86accd07d16d3f952c4237d779c43de77ae13be
related_topics:
  - title: English version
    url: /en/android/pm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/pm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/pm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/pm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/pm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/pm.html
    icon: bi bi-globe
---
# pm

Zeige Informationen über Apps auf einem Android Gerät.
Weitere Informationen: <https://developer.android.com/studio/command-line/adb#pm>.

- Gib eine Liste aller installierten Apps aus:

`pm list packages`

- Gib eine Liste aller installierten System-Apps aus:

`pm list packages -s`

- Gib eine Liste aller installierten Apps von Drittanbietern aus:

`pm list packages -3`

- Gib eine Liste aller Apps, auf die ein bestimmtes Schlüsselwort zutrifft, aus:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Schlüsselwort</span>

- Gib den Pfad der APK einer bestimmten App aus:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app</span>
