---
layout: page
title: android/dumpsys (français)
description: "Fourni des informations sur les services du système Android."
content_hash: 6e3de76e5faf82be26d8702b78b064da2bd91447
related_topics:
  - title: Deutsch version
    url: /de/android/dumpsys.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/dumpsys.html
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

Fourni des informations sur les services du système Android.
Cette commande peut être utilisé uniquement depuis `adb shell`.
Plus d'informations : <https://developer.android.com/studio/command-line/dumpsys>.

- Récupère un diagnostic pour chaque service système :

`dumpsys`

- Récupère un diagnostic pour un service système spécifique :

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>

- Liste tous les services dont `dumpsys` peut donner les informations :

`dumpsys -l`

- Liste les arguments spécifiques d'un service :

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>` -h`

- Exclus un service spécifique d'un diagnostic :

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>

- Spécifie un temps limite en secondes (10s par défault) :

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>
