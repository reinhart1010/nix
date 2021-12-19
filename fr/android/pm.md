---
layout: page
title: android/pm (français)
description: "Afficher des informations sur les applications d'un appareil Android."
content_hash: 27390286384b387a90ccbf243630b272bef80b64
related_topics:
  - title: Deutsch version
    url: /de/android/pm.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/pm.html
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

Afficher des informations sur les applications d'un appareil Android.
Plus d'informations : <https://developer.android.com/studio/command-line/adb#pm>.

- Affiche la liste des applications installées :

`pm list packages`

- Affiche une liste de toutes les applications système instalées :

`pm list packages -s`

- Affiche une liste de toutes les applications tierces :

`pm list packages -3`

- Affiche une liste des applications qui correspondent à des mots clés :

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mots_clés</span>

- Affiche le chemin vers l'APK d'une application spécifique :

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application</span>
