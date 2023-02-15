---
layout: page
title: common/arping (français)
description: "Découvre et sonde des hôtes dans un réseau en utilisant le protocol ARP."
content_hash: 0d9f61b3312c97e98f9a26cbcb3360badf07cc21
last_modified_at: 2023-02-15
related_topics:
  - title: English version
    url: /en/common/arping.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/arping.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arping.html
    icon: bi bi-globe
---
# arping

Découvre et sonde des hôtes dans un réseau en utilisant le protocol ARP.
Très utile pour la découverte d'adresse MAC.
Plus d'informations : <https://github.com/ThomasHabets/arping>.

- Ping un hôte par paquets de requête ARP :

`arping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_hôte</span>

- Ping un hôte sur une interface spécifique :

`arping -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_hôte</span>

- Ping un hôte et arrête à la première réponse :

`arping -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_hôte</span>

- Ping un hôte un certain nombre de fois :

`arping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_d_appel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_hôte</span>

- Diffuse les paquets de requête ARP pour mettre à jour les caches ARP voisin :

`arping -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_à_diffuser</span>

- Détecte les adresses IP dupliquées dans le réseau en envoyant les requêtes ARP avec une expiration de 3 secondes :

`arping -D -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_à_vérifier</span>
