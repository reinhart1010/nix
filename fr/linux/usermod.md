---
layout: page
title: linux/usermod (français)
description: "Modifie un compte utilisateur."
content_hash: df3204f1cd75946e10bd7ee229ce7061f55e9466
related_topics:
  - title: English version
    url: /en/linux/usermod.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/usermod.html
    icon: bi bi-globe
---
# usermod

Modifie un compte utilisateur.
Plus d'informations : <https://manned.org/usermod>.

- Change le nom d'un utilisateur :

`usermod -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_nom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>

- Ajoute l'utilisateur à des groupes supplémentaires (attention à l'omission d'espaces) :

`usermod -a -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groupe1,groupe2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>

- Crée un nouveau dossier home pour un utilisateur et déplace ses fichiers vers celui-ci :

`usermod -m -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/home</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>
