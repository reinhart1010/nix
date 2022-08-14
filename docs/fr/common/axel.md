---
layout: page
title: common/axel (français)
description: "Accélérateur de téléchargement."
content_hash: 5d113fbc4366b80a81a1f70238495ddb61e7902e
related_topics:
  - title: English version
    url: /en/common/axel.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/axel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/axel.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/axel.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/axel.html
    icon: bi bi-globe
---
# axel

Accélérateur de téléchargement.
Supporte HTTP, HTTPS, et FTP.
Plus d'informations : <https://github.com/axel-download-accelerator/axel>.

- Télécharge depuis une URL vers un fichier :

`axel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Télécharge et spécifie le nom de fichier :

`axel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_fichier</span>

- Télécharge avec plusieurs connections :

`axel -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_connections</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Recherche des miroirs :

`axel -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_miroirs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Limite la vitesse de téléchargement (en octets par secondes) :

`axel -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vitesse</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
