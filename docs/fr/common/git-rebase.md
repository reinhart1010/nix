---
layout: page
title: common/git-rebase (français)
description: "Rejoue les commits d'une branche par dessus une autre."
content_hash: 6eef9c027e6ef32524ef5af2f4126a02b09273d6
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-rebase.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-rebase.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rebase.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rebase.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-rebase.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-rebase.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rebase.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-rebase.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-rebase.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rebase

Rejoue les commits d'une branche par dessus une autre.
Communément utilisé pour dupliquer les commits d'une branche dans une autre, en créant de nouveaux commits dans la branche de destination.
Plus d'informations : <https://git-scm.com/docs/git-rebase>.

- Rejouer les commits de la branche courante sur la branche master :

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master</span>

- Rejouer les comits interactivement, ce qui permet aux commits d'être re-arrangés, exclus, combinés ou modifiés :

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branche_de_base_ou_commit</span>

- Continuer le re-jeu des commits après la résolution d'un conflit :

`git rebase --continue`

- Continuer le re-jeu des commits en sautant la résolution d'un conflit :

`git rebase --skip`

- Annule l'opération (ex : en cas de conflit) :

`git rebase --abort`

- Déplacez une partie de la branche actuelle sur une nouvelle base, fournissant l'ancienne base à partir de laquelle commencer :

`git rebase --onto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_base</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_base</span>

- Rejoue les 5 derniers commits, ce qui permet aux commits d'être re-arrangés, exclus, combinés ou modifiés :

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~5</span>

- Résoudre automatiquement les conflits en précisant la version à conserver (`theirs` signifie la version des fichiers à privilégier) :

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-X|--strategy-option</span>` theirs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master</span>
