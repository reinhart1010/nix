---
layout: page
title: sunos/snoop (français)
description: "Renifleur de paquets réseau."
content_hash: 1fdd31babd6bc7d40db331e26a844116cb5bd45f
related_topics:
  - title: বাংলা version
    url: /bn/sunos/snoop.html
    icon: bi bi-globe
  - title: English version
    url: /en/sunos/snoop.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/snoop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/snoop.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/snoop.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># snoop

Renifleur de paquets réseau.
Équivalent SunOS de tcpdump.
Plus d'information : <https://www.unix.com/man-page/sunos/1m/snoop>.

- Capturer des paquets sur une interface réseau spécifique :

`snoop -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">e1000g0</span>

- Enregistrer les paquets capturés dans un fichier au lieu de les afficher :

`snoop -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_fichier</span>

- Afficher le résumé détaillé de la couche de protocole des paquets d'un fichier :

`snoop -V -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_fichier</span>

- Capturez les paquets réseau provenant d'un nom d'hôte et accédez à un port donné :

`snoop to port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` from host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d'hôte</span>

- Capturez et affichez un vidage hexadécimal des paquets réseau échangés entre deux adresses IP :

`snoop -x0 -p4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse_ip_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse_ip_2</span>
