---
layout: page
title: common/git-update-index (français)
description: "Commande Git pour manipuler l'index."
content_hash: 5aa82366356240205934ba8e17c15e12764ab2d7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-update-index.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-update-index.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git update-index

Commande Git pour manipuler l'index.
Plus d'informations : <https://git-scm.com/docs/git-update-index>.

- Prétendre qu'un fichier modifié est inchangé (`git status` ne l'affichera pas comme modifié) :

`git update-index --skip-worktree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_modifié</span>
