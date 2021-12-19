---
layout: page
title: common/git-diff (italiano)
description: "Mostra le modifiche ai file tracciati."
content_hash: e3c54a6bc76890e74b972e192cb28649b21bc712
related_topics:
  - title: English version
    url: /en/common/git-diff.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-diff.html
    icon: bi bi-globe
---
# git diff

Mostra le modifiche ai file tracciati.
Maggiori informazioni: <https://git-scm.com/docs/git-diff>.

- Mostra le modifiche non ancora nell'area di stage:

`git diff`

- Mostra tutte le modifiche non ancora salvate in un commit (incluse quelle nell'area di stage):

`git diff HEAD`

- Mostra solo le modifiche nell'area di stage (aggiunte, ma non ancora committate):

`git diff --staged`

- Mostra le modifiche di tutti i commit a partire da una certa data/ora (un'espressione temporale come "1 week 2 days" o una data ISO):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Mostra solo i nomi dei file modificati a partire da un dato commit:

`git diff --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Stampa un riepilogo dei file creati, rinominati o la cui modalità è cambiata a partire da un dato commit:

`git diff --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Confronta le versioni di un dato file tra due rami o commit:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo_2</span>` [--] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>

- Confronta le versioni di più file tra il ramo corrente e un altro ramo:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>
