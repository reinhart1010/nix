---
layout: page
title: common/androguard (français)
description: "Outil d’ingénierie inverse pour les applications Android. Écrit en Python."
content_hash: 0cb4d8ebe43c3921a54a6447df5b37f706f9d6e6
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/androguard.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/androguard.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/androguard.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/androguard.html
    icon: bi bi-globe
tldri18n_status: 2
---
# androguard

Outil d’ingénierie inverse pour les applications Android. Écrit en Python.
Plus d'informations : <https://github.com/androguard/androguard>.

- Affiche le manifest d'application Android :

`androguard axml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/app.apk</span>

- Affiche les métadonnées de l'application (version et ID d'application) :

`androguard apkid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/app.apk</span>

- Décompile le code Java de l'application :

`androguard decompile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/app.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>
