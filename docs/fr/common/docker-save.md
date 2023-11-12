---
layout: page
title: common/docker-save (français)
description: "Exporeter une ou plusieurs images Docker dans une archive."
content_hash: da14fc60e89ac72cf1399d5e23745a3b3164c9f5
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-save.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-save.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-save.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-save.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker save

Exporeter une ou plusieurs images Docker dans une archive.
Plus d'informations : <https://docs.docker.com/engine/reference/commandline/save/>.

- Sauvegarder une image en redirigeant la sortie standard vers une archive tar :

`docker save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etquette</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.tar</span>

- Sauvegarder une image dans une archive tar :

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etquette</span>

- Sauvegarder toutes les étiquettes de l'image :

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l_image</span>

- Sélectionner des étiquettes particulières d'une image à sauvegarder :

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l_image:etquette1 nom_de_l_image:etquette2 ...</span>
