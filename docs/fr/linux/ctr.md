---
layout: page
title: linux/ctr (français)
description: "Gère les conteneurs et images de `containerd`."
content_hash: bbe4b2ff99b9208ea3d735840226669229d2bb78
related_topics:
  - title: English version
    url: /en/linux/ctr.html
    icon: bi bi-globe
---
# ctr

Gère les conteneurs et images de `containerd`.
Plus d'informations : <https://containerd.io>.

- Liste tous les conteneurs (en marche et arrêtés) :

`ctr containers list`

- Liste toutes les images :

`ctr images list`

- Télécharge une image :

`ctr images pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Étiquette une image :

`ctr images tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_source</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">étiquette_source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_destination</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">étiquette_destination</span>
