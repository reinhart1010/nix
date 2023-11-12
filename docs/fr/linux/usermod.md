---
layout: page
title: linux/usermod (français)
description: "Modifie le compte d'un utilisateur."
content_hash: bbc4d3893095400cee85e90097332bdf761aca26
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/usermod.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/usermod.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/usermod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# usermod

Modifie le compte d'un utilisateur.
Voir aussi `users`, `useradd`, `userdel`.
Plus d'informations : <https://manned.org/usermod>.

- Change le nom d'un utilisateur :

`sudo usermod --login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_nom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Modifie l'identifiant numérique d'un utilisateur :

`sudo usermod --uid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifiant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Change le shell d'un utilisateur :

`sudo usermod --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Ajoute l'utilisateur à des groupes supplémentaires (attention à l'omission d'espaces) :

`sudo usermod --append --groups `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groupe1,groupe2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Change le répertoire personnel d'un utilisateur et déplace ses fichiers vers celui-ci :

`sudo usermod --move-home --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/nouveau_répertoire</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>
