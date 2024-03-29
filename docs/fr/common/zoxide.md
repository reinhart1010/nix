---
layout: page
title: common/zoxide (français)
description: "Garde une trace des répertoires les plus utilisés."
content_hash: ea4a843e5d215cffb29e0ec888ff316af1e719ec
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/zoxide.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/zoxide.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zoxide

Garde une trace des répertoires les plus utilisés.
Utilise un algorithme de classement pour identifier le meilleur résultat.
Plus d'informations : <https://github.com/ajeetdsouza/zoxide>.

- Aller au répertoire avec le meilleur classement qui contient "foo" dans son nom :

`zoxide query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Aller au répertoire avec le meilleur classement qui contient "foo" et "bar" dans son nom :

`zoxide query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- Démarre une recherche de répertoire interactive (nécessite `fzf`) :

`zoxide query --interactive`

- Ajoute un répertoire ou incrémente son classement :

`zoxide add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/du/répertoire</span>

- Supprime un répertoire interactive de la base de données de `zoxide` :

`zoxide remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/du/répertoire</span>` --interactive`

- Génère la configuration du shell pour la mise en place des alias de commandes (`z`, `za`, `zi`, `zq`, `zr`) :

`zoxide init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|zsh</span>
