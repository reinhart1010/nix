---
layout: page
title: common/deluge (français)
description: "Client BitTorrent à base de ligne de commande."
content_hash: 11261c032d97017f3c4aa57031be2a254e895e88
related_topics:
  - title: English version
    url: /en/common/deluge.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/deluge.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/deluge.html
    icon: bi bi-globe
---
# deluge

Client BitTorrent à base de ligne de commande.
Plus d'informations : <https://deluge-torrent.org>.

- Télécharge un torrent :

`deluge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|chemin/vers/fichier</span>

- Télécharge un torrent à l'aide d'un fichier de configuration particulier :

`deluge -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_configuration</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|chemin/vers/fichier</span>

- Télécharge un torrent et lance un interface usager particulier :

`deluge -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gtk|web|console</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|chemin/vers/fichier</span>

- Télécharge un torrent et enregistre les journaux dans un ficher :

`deluge -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_journalisation</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|chemin/vers/fichier</span>
