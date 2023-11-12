---
layout: page
title: common/adb-shell (français)
description: "Android Debug Bridge Shell: Exécute une commande shell sur une instance d'émulateur Android ou un appareil Android."
content_hash: f9bd40b8c86bfe85b04eee0418014b478a0d8b49
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/adb-shell.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-shell.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/adb-shell.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-shell.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-shell.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-shell.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-shell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-shell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-shell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-shell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb shell

Android Debug Bridge Shell: Exécute une commande shell sur une instance d'émulateur Android ou un appareil Android.
Plus d'informations : <https://developer.android.com/studio/command-line/adb>.

- Démarre une session shell interactive sur l'émulateur/l'appareil :

`adb shell`

- Récupère toutes les propriétés depuis un émulateur ou un appareil :

`adb shell getprop`

- Remet toutes les permissions courante à leurs valeurs par défaut :

`adb shell pm reset-permissions`

- Révoque une permission dangereuse pour une application :

`adb shell pm revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">permission</span>

- Déclenche un événement clé :

`adb shell input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Nettoie les données d'une application sur un émulateur ou un appareil :

`adb shell pm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Démarre une activité sur un émulateur ou un appareil :

`adb shell am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">activité</span>

- Démarre une activité maison depuis un émulateur ou un appareil :

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
