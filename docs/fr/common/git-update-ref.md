---
layout: page
title: common/git-update-ref (français)
description: "Commande Git pour créer, mettre à jour et supprimer des références Git."
content_hash: 1caaf2223c100c8a3c5bc03d15432d526dc9e5fa
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-update-ref.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-update-ref.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-update-ref.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git update-ref

Commande Git pour créer, mettre à jour et supprimer des références Git.
Plus d'informations : <https://git-scm.com/docs/git-update-ref>.

- Supprimer une référence, utile pour la réinitialisation du premier commit :

`git update-ref -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Mettre a jour une référence avec un message :

`git update-ref -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4e95e05</span>
