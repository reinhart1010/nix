---
layout: page
title: common/aapt (français)
description: "Android Asset Packaging Tool."
content_hash: 0a6b71eb67ebf5f0c8326d13177d230f9b701a89
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/aapt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/aapt.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aapt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aapt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/aapt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aapt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aapt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aapt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aapt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/aapt.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aapt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aapt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aapt

Android Asset Packaging Tool.
Compile et empaquette les ressources d'une application Android.
Plus d'informations : <https://elinux.org/Android_aapt>.

- Liste les fichiers contenus une archive APK :

`aapt list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/app.apk</span>

- Affiche les metadatas d'une application (version, autorisations, etc.) :

`aapt dump badging `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/app.apk</span>

- Créé une nouvelle archive APK avec les fichiers venant d'un dossier spécifique :

`aapt package -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/app.apk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/dossier</span>
