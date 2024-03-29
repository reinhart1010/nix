---
layout: page
title: common/git-show-branch (français)
description: "Affiche les branches et leurs commits."
content_hash: 1af0e743defc4002383f905846fa51a06ffd8529
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/git-show-branch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-show-branch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-show-branch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git show-branch

Affiche les branches et leurs commits.
Plus d'informations : <https://git-scm.com/docs/git-show-branch>.

- Affiche un résumé du dernier commit dans la branche :

`git show-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche|ref|commit</span>

- Comparer des commits avec plusieurs commits ou branches :

`git show-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche|ref|commit</span>

- Comparer toutes les branches distantes :

`git show-branch --remotes`

- Comparer la branche locale avec la branche distante :

`git show-branch --all`

- Lister les derniers commits sur toutes les branches :

`git show-branch --all --list`

- Comparer une branche spécifique à la branche courante :

`git show-branch --current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit|nom_de_branche|ref</span>

- Afficher le nom du commit au lieu du nom relatif :

`git show-branch --sha1-name --current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">current|nom_de_branche|ref</span>

- Continuez l'affichage d'un certain nombre de commits au-delà de l'ancêtre commun :

`git show-branch --more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit|nom_de_branche|ref</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit|nom_de_branche|ref</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>
