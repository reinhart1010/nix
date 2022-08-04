---
layout: page
title: linux/useradd (français)
description: "Crée un nouvel utilisateur."
content_hash: d23c3c8fbc6d56f7afadef45ca45220c518676a8
related_topics:
  - title: English version
    url: /en/linux/useradd.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/useradd.html
    icon: bi bi-globe
---
# useradd

Crée un nouvel utilisateur.
Plus d'informations : <https://manned.org/useradd>.

- Crée un nouvel utilisateur :

`useradd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Crée un nouvel utilisateur avec un dossier home par défaut :

`useradd --create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Crée un nouvel utilisateur avec le shell spécifié :

`useradd --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Crée un nouvel utilisateur qui appartient aux groupes supplémentaires (attention à l'omission des espaces) :

`useradd --groups `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groupe1,groupe2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Crée un nouvel utilisateur sans un dossier home :

`useradd --no-create-home --system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>
