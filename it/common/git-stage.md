---
layout: page
title: common/git-stage (italiano)
description: "Aggiungi file all'area di stage."
content_hash: 816c7e637b928c3359b1bdf92236285fe57e0915
related_topics:
  - title: English version
    url: /en/common/git-stage.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-stage.html
    icon: bi bi-globe
---
# git stage

Aggiungi file all'area di stage.
Sinonimo di `git add`.
Maggiori informazioni: <https://git-scm.com/docs/git-stage>.

- Aggiungi un file all'indice:

`git stage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>

- Aggiungi tutti i file (tracciati e non):

`git stage -A`

- Aggiungi solo file già tracciati:

`git stage -u`

- Aggiungi anche file ignorati:

`git stage -f`

- Aggiungi parti di file all'area di stage in modo interattivo:

`git stage -p`

- Aggiungi parti di un dato file all'area di stage in modo interattivo:

`git stage -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>

- Aggiungi all'area di stage in modo interattivo:

`git stage -i`
