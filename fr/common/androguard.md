---
layout: page
title: common/androguard (français)
description: "Outil d’ingénierie inverse pour les applications Android. Écrit en Python."
content_hash: 8d52d8ef180bd66091b42088bcb503fdac690c20
related_topics:
  - title: English version
    url: /en/common/androguard.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/androguard.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># androguard

Outil d’ingénierie inverse pour les applications Android. Écrit en Python.
Plus d'informations : <https://github.com/androguard/androguard>.

- Affiche le manifest d'application Android :

`androguard axml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/app.apk</span>

- Affiche les métadonnées de l'application (version et id d'application) :

`androguard apkid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/app.apk</span>

- Décompile le code Java de l'application :

`androguard decompile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/app.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>
