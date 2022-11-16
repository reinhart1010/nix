---
layout: page
title: common/jekyll (français)
description: "Générateur de site statique simple, adapté aux blogs."
content_hash: e0b9af40b62d9ed05123d5543696b410b682c07d
related_topics:
  - title: English version
    url: /en/common/jekyll.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/jekyll.html
    icon: bi bi-globe
---
# jekyll

Générateur de site statique simple, adapté aux blogs.
Plus d'informations : <https://jekyllrb.com/docs/usage/>.

- Génère un serveur de développement qui tourne en http://localhost:4000/ :

`jekyll serve`

- Active la régénération incrémentale :

`jekyll serve --incremental`

- Active la sortie verbeuse :

`jekyll serve --verbose`

- Génère le répertoire actuel dans `./_site` :

`jekyll build`

- Nettoie le site (c.-à.-d. supprime la sortie du site et le répertoire `cache`) sans compiler :

`jekyll clean`
