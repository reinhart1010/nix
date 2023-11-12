---
layout: page
title: common/ftp (français)
description: "Outils permettant d'interagir avec un serveur avec le protocole FTP."
content_hash: 04af4904e19b734fae7ee5df39c1d4dc64137e31
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ftp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ftp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ftp

Outils permettant d'interagir avec un serveur avec le protocole FTP.
Plus d'informations : <https://manned.org/ftp>.

- Connexion à un serveur FTP :

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp.exemple.com</span>

- Connexion à un serveur FTP en spécifiant son adresse IP et son port :

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse_IP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Passe en mode de transfert binaire (médias, fichiers compressés, etc) :

`binary`

- Transfère plusieurs fichiers sans demander de confirmation pour chaque :

`prompt off`

- Télécharge plusieurs fichiers :

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- Téléverse plusieurs fichiers :

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- Supprime plusieurs fichiers sur le serveur distant :

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- Renomme un fichier sur le serveur distant :

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancien_fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_fichier</span>
