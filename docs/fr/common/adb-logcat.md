---
layout: page
title: common/adb-logcat (français)
description: "Jeter une log des messages systèmes."
content_hash: 01cd335b18755a0e923204ba7ecef231928c546e
related_topics:
  - title: English version
    url: /en/common/adb-logcat.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adb-logcat

Jeter une log des messages systèmes.
Plus d'informations : <https://developer.android.com/studio/command-line/logcat>.

- Affiche les logs systèmes :

`adb logcat`

- Affiche les logs qui correspond à une expression régulière :

`adb logcat -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_régulière</span>

- Affiche les logs pour un tag donné, dans un mode spécifique ([V]erbose, [D]ebug, [I]nfo, [W]arning, [E]rror, [F]atal, [S]ilent) :

`adb logcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mode</span>` *:S`

- Affiche les logs pour des applications React Native en mode [V]erbose et mes sous [S]ilence les autres tags :

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Affiche les logs avec un niveau de priorité supérieur à [W]arning :

`adb logcat *:W`

- Colorie les logs (souvent utilisé avec des filtres) :

`adb logcat -v color`
