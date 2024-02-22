---
layout: page
title: common/adb-reverse (français)
description: "Android Debug Bridge Reverse: Transfère des connections réseaux depuis une instance d'émulateur Android ou un appareil Android."
content_hash: 8af871107c092aaafdefa8726d45b0dea2419ec5
last_modified_at: 2024-02-22
related_topics:
  - title: English version
    url: /en/common/adb-reverse.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-reverse.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-reverse.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-reverse.html
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
tldri18n_status: 2
---
# adb reverse

Android Debug Bridge Reverse: Transfère des connections réseaux depuis une instance d'émulateur Android ou un appareil Android.
Plus d'informations : <https://developer.android.com/tools/adb>.

- Affiche la liste de toutes les connections réseaux qui sont transféré depuis les émulateurs ou les appareils :

`adb reverse --list`

- Transfère un port TCP depuis un émulateur ou un appareil vers localhost :

`adb reverse tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_distant</span>` tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_local</span>

- Supprime une connection socket en cours depuis un émulateur ou un appareil :

`adb reverse --remove tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_distant</span>

- Supprime toutes les connections socket depuis tous les émulateurs et appareils :

`adb reverse --remove-all`
