---
layout: page
title: common/acyclic (français)
description: "Construit un graphe orienté acyclique en inversant quelques sommets."
content_hash: c9b24e6f999de0ff1c5982444e8afc3f3a823ed6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/acyclic.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/acyclic.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acyclic.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acyclic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# acyclic

Construit un graphe orienté acyclique en inversant quelques sommets.
Filtres Graphviz : `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
Plus d'informations : <https://graphviz.org/pdf/acyclic.1.pdf>.

- Construit un graphe orienté acyclique en inversant quelques sommets :

`acyclic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/entrée.gv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/sortie.gv</span>

- Affiche si un graphe est acyclique, possède une boucle ou est non-dirigé, ne produit pas de graphe en sortie :

`acyclic -v -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/entrée.gv</span>

- Affiche l'aide d' `acyclic` :

`acyclic -?`
