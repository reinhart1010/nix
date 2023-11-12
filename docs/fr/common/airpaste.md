---
layout: page
title: common/airpaste (français)
description: "Partage des messages et des fichiers sur le même réseau en utilisant mDNS."
content_hash: 05665f801c5030aac01594ef1467ffafe4c0ccef
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/airpaste.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airpaste.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/airpaste.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/airpaste.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airpaste.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/airpaste.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airpaste.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airpaste

Partage des messages et des fichiers sur le même réseau en utilisant mDNS.
Plus d'informations : <https://github.com/mafintosh/airpaste>.

- Attend un message et l'affiche une fois reçu :

`airpaste`

- Envoie un message :

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` | airpaste`

- Envoie un fichier :

`airpaste < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Recevoir un fichier :

`airpaste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Crée ou rejoins un canal :

`airpaste `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_canal</span>
