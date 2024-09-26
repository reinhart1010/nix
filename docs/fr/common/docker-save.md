---
layout: page
title: common/docker-save (français)
description: "Exporeter une ou plusieurs images Docker dans une archive."
content_hash: b69330aa7c8ba7ec04077fe4c2edc69075a6d32b
last_modified_at: 2024-09-26
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
Plus d'informations : <https://docs.docker.com/reference/cli/docker/image/save/>.

- Sauvegarder une image en redirigeant la sortie standard vers une archive tar :

`docker save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etquette</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.tar</span>

- Sauvegarder une image dans une archive tar :

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etquette</span>

- Sauvegarder toutes les étiquettes de l'image :

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l_image</span>

- Sélectionner des étiquettes particulières d'une image à sauvegarder :

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l_image:etquette1 nom_de_l_image:etquette2 ...</span>
