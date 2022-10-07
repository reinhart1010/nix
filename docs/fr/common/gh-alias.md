---
layout: page
title: common/gh-alias (français)
description: "Gérer les alias de commandes GitHub CLI depuis la ligne de commande."
content_hash: 2aa1bf70167c789d38e806f9782c75f68345c52f
related_topics:
  - title: English version
    url: /en/common/gh-alias.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gh alias

Gérer les alias de commandes GitHub CLI depuis la ligne de commande.
Plus d'informations : <https://cli.github.com/manual/gh_alias>.

- Affiche l'aide pour la sous-commande `alias` :

`gh alias`

- Liste tous les alias pour lesquels `gh` est configuré :

`gh alias list`

- Crée un alias de sous-commande pour `gh` :

`gh alias set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande_gh</span>

- Définit une commande shell comme sous-commande de `gh` :

`gh alias set --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l'alias</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Supprime un alias :

`gh alias delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l'alias</span>
