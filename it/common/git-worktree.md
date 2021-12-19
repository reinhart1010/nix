---
layout: page
title: common/git-worktree (italiano)
description: "Gestisci gli alberi di lavoro collegati allo stesso repository."
content_hash: feebb98583b5890a80514c1e6b8dc05658803a0d
related_topics:
  - title: English version
    url: /en/common/git-worktree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-worktree.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-worktree.html
    icon: bi bi-globe
---
# git worktree

Gestisci gli alberi di lavoro collegati allo stesso repository.
Maggiori informazioni: <https://git-scm.com/docs/git-worktree>.

- Crea una nuova cartella a partire da uno specifico ramo:

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/cartella</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo</span>

- Crea una nuova cartella a partire da un nuovo ramo:

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/cartella</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuovo_ramo</span>

- Mostra tutte le cartelle di lavoro collegate al repository corrente:

`git worktree list`

- Cancella un albero di lavoro (dopo averne cancellato la cartella):

`git worktree prune`
