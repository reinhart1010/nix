---
layout: page
title: linux/userdel (français)
description: "Supprime un compte utilisateur ou supprime un utilisateur d'un groupe."
content_hash: 80920f5b26c22c12f42bbb4d39701674d1f3a9a7
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/userdel.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/userdel.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/userdel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# userdel

Supprime un compte utilisateur ou supprime un utilisateur d'un groupe.
Voir aussi `users`, `useradd`, `usermod`.
Plus d'informations : <https://manned.org/userdel>.

- Supprime un utilisateur :

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Supprime un utilisateur dans un autre répertoire racine :

`sudo userdel --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/autre_racine</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>

- Supprime un utilisateur, son répertoire personnel ainsi que son répertoire d'attente des courriels :

`sudo userdel --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>
