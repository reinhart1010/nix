---
layout: page
title: common/adb-install (français)
description: "Android Debug Bridge Install: Pousse des paquets vers une instance d'émulateur Android ou un appareil Android."
content_hash: 0ed0bd3bbc199fd5f219a80a1aae2aa56d0c72d8
last_modified_at: 2024-02-22
related_topics:
  - title: English version
    url: /en/common/adb-install.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-install.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-install.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-install.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb install

Android Debug Bridge Install: Pousse des paquets vers une instance d'émulateur Android ou un appareil Android.
Plus d'informations : <https://developer.android.com/tools/adb>.

- Pousse une application Android vers l'émulateur/l'appareil :

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier.apk</span>

- Pousse une application Android vers l'émulateur/l'appareil spécifique via son numéro de série (écrase la variable `$ANDROID_SERIAL`):

`adb -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_de_serie</span>` install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier.apk</span>

- Réinstalle une application existante, tout en gardant ses données :

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier.apk</span>

- Pousse une application Android en autorisant la rétrogradation de version (uniquement pour les paquets debuggable) :

`adb install -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier.apk</span>

- Accorde toutes les permissions listées dans le manifeste de l'application :

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier.apk</span>

- Mets à jour rapidement un paquet en mettant à jour uniquement les parties de l'APK qui ont changé :

`adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier.apk</span>
