---
layout: page
title: common/git-reset (italiano)
description: "Annulla commit o rimuovi modifiche dall'area di stage, reimpostando l'HEAD corrente su uno specifico stato."
content_hash: ae15ec0c0858e5c6a9bf4c380e2853541dee81f2
related_topics:
  - title: English version
    url: /en/common/git-reset.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-reset.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-reset.html
    icon: bi bi-globe
---
# git reset

Annulla commit o rimuovi modifiche dall'area di stage, reimpostando l'HEAD corrente su uno specifico stato.
Se viene fornito un percorso, il comando reset si interpreta come "rimuovi dall'area di stage"; se viene fornito l'hash di un commit o un ramo, si interpreta come "annulla commit".
Maggiori informazioni: <https://git-scm.com/docs/git-reset>.

- Rimuovi tutto dall'area di stage:

`git reset`

- Rimuovi dall'area di stage uno o più file:

`git reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file2</span>

- Rimuovi dall'area di stage solo alcune porzioni di un file in modo interattivo:

`git reset --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>

- Annulla l'ultimo commit, preservando tutte le modifiche nel filesystem:

`git reset HEAD~`

- Annulla gli ultimi due commit, aggiungendo all'area di stage le modifiche relative:

`git reset --soft HEAD~2`

- Annulla le modifiche non committate, indipendentemente se siano presenti nell'area di stage o meno (usa `git checkout` per queste ultime):

`git reset --hard`

- Reimposta il repository su un dato commit, annullando qualsiasi tipo di modifica precedente:

`git reset --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
