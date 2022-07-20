---
layout: page
title: common/acyclic (français)
description: "Construit un graphe orienté acyclique en inversant quelques sommets."
content_hash: c9b24e6f999de0ff1c5982444e8afc3f3a823ed6
related_topics:
  - title: English version
    url: /en/common/acyclic.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># acyclic

Construit un graphe orienté acyclique en inversant quelques sommets.
Filtres Graphviz : `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
Plus d'informations : <https://graphviz.org/pdf/acyclic.1.pdf>.

- Construit un graphe orienté acyclique en inversant quelques sommets :

`acyclic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/entrée.gv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/sortie.gv</span>

- Affiche si un graphe est acyclique, possède une boucle ou est non-dirigé, ne produit pas de graphe en sortie :

`acyclic -v -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/entrée.gv</span>

- Affiche l'aide d' `acyclic` :

`acyclic -?`
