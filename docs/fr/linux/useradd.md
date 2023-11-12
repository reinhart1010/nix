---
layout: page
title: linux/useradd (français)
description: "Crée un nouvel utilisateur."
content_hash: d0b8c66d6d930697dc2bb59db6d727bd764a2232
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/useradd.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/useradd.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/useradd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# useradd

Crée un nouvel utilisateur.
Voir aussi `users`, `userdel`, `usermod`.
Plus d'informations : <https://manned.org/useradd>.

- Crée un nouvel utilisateur :

`sudo useradd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Crée un nouvel utilisateur en spéficiant un identifiant numérique particulier :

`sudo useradd --uid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifiant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Crée un nouvel utilisateur avec le shell spécifié :

`sudo useradd --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Crée un nouvel utilisateur qui appartient aux groupes supplémentaires (attention à l'omission des espaces) :

`sudo useradd --groups `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groupe1,groupe2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Crée un nouvel utilisateur avec le répertoire personnel par défaut :

`sudo useradd --create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Crée un nouvel utilisateur avec un répertoire personnel rempli par les fichiers et répertoires d'un répertoire squelette :

`sudo useradd --skel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/repertoire_squelette</span>` --create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Crée un nouvel utilisateur système sans répertoire personnel :

`sudo useradd --system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>
