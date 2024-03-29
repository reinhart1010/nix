---
layout: page
title: common/airshare (français)
description: "Transférer des données entre deux machines dans un réseau local."
content_hash: 21de47d19c6eb3ff980f2ec12e1e145cf0f381f9
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/common/airshare.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/airshare.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airshare.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airshare

Transférer des données entre deux machines dans un réseau local.
Plus d'informations : <https://airshare.rtfd.io/en/latest/cli.html>.

- Partager des fichiers ou des dossiers :

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_dossier1 chemin/vers/fichier_ou_dossier2 ...</span>

- Recevoir un fichier :

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Héberger un serveur de réception (utilisez ceci pour pouvoir télécharger des fichiers via l'interface web) :

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Envoyer des fichiers ou des dossiers a un serveur de reception :

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_dossier1 chemin/vers/fichier_ou_dossier2 ...</span>

- Envoyer les fichiers dont les chemins ont été copiés dans le presse-papiers :

`airshare --file-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Recevoir un fichier et le copier dans le presse-papier :

`airshare --clip-receive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>
