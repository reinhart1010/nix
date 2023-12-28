---
layout: page
title: common/gh-alias (français)
description: "Gérer les alias de commandes GitHub CLI depuis la ligne de commande."
content_hash: ea8dd275f61ed6c1f2a78401a0ef1290edb3ee21
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/gh-alias.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh alias

Gérer les alias de commandes GitHub CLI depuis la ligne de commande.
Plus d'informations : <https://cli.github.com/manual/gh_alias>.

- Affiche l'aide pour la sous-commande `alias` :

`gh alias`

- Liste tous les alias pour lesquels `gh` est configuré :

`gh alias list`

- Crée un alias de sous-commande pour `gh` :

`gh alias set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande_gh</span>`'`

- Définit une commande shell comme sous-commande de `gh` :

`gh alias set --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l'alias</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Supprime un alias :

`gh alias delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l'alias</span>
