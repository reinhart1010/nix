---
layout: page
title: common/git-worktree (italiano)
description: "Gestisci gli alberi di lavoro collegati allo stesso repository."
content_hash: e344feb058509c531db3324b20708eeb641209e0
last_modified_at: 2023-11-12
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
  - title: Türkçe version
    url: /tr/common/git-worktree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git worktree

Gestisci gli alberi di lavoro collegati allo stesso repository.
Maggiori informazioni: <https://git-scm.com/docs/git-worktree>.

- Crea una nuova directory a partire da uno specifico ramo:

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo</span>

- Crea una nuova directory a partire da un nuovo ramo:

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuovo_ramo</span>

- Mostra tutte le directory di lavoro collegate al repository corrente:

`git worktree list`

- Cancella un albero di lavoro (dopo averne cancellato la directory):

`git worktree prune`
