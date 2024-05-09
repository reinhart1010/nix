---
layout: page
title: common/adb-logcat (français)
description: "Jeter une log des messages systèmes."
content_hash: 2ea60a0ffffb57e333a65b88dc45bce2a93169f5
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/common/adb-logcat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-logcat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-logcat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-logcat.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adb logcat

Jeter une log des messages systèmes.
Plus d'informations : <https://developer.android.com/tools/logcat>.

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
