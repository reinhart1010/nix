---
layout: page
title: common/adb (français)
description: "Android Debug Bridge: Communiquer avec une instance d'émulateur Android ou un appareil Android."
content_hash: 65939902e2d3a1107485288c4788f0ebd7b441d6
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/common/adb.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/adb.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adb

Android Debug Bridge: Communiquer avec une instance d'émulateur Android ou un appareil Android.
Certaines commandes comme `adb shell` ont leur propre documentation.
Plus d'informations : <https://developer.android.com/tools/adb>.

- Vérifie si le processus du serveur adb est en fonctionnement et le démarre :

`adb start-server`

- Arrête le processus du serveur adb :

`adb kill-server`

- Démarre un shell distant sur l'émulateur/l'appareil ciblé :

`adb shell`

- Pousse une application Android vers l'émulateur/l'appareil :

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier.apk</span>

- Copie un fichier/dossier depuis l'appareil ciblé :

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier_ou_dossier_de_l'appareil</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/dossier_de_destination_local</span>

- Copie un fichier/dossier vers l'appareil ciblé :

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier_ou_dossier_local</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/dossier_de_destination_de_l'appareil</span>

- Récupère une liste des appareils connectés :

`adb devices`
