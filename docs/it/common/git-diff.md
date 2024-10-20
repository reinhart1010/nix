---
layout: page
title: common/git-diff (italiano)
description: "Mostra le modifiche ai file tracciati."
content_hash: bf8c00da48eb4dfaa4e475a65061b910e050115a
last_modified_at: 2024-10-20
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
  - title: 한국어 version
    url: /ko/common/git-diff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-diff.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-diff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git diff

Mostra le modifiche ai file tracciati.
Maggiori informazioni: <https://git-scm.com/docs/git-diff>.

- Mostra le modifiche non ancora nell'area di stage:

`git diff`

- Mostra tutte le modifiche non ancora salvate in un commit (incluse quelle nell'area di stage):

`git diff HEAD`

- Mostra solo le modifiche nell'area di stage (aggiunte, ma non ancora aggiunte ad un commit):

`git diff --staged`

- Mostra le modifiche di tutti i commit a partire da una certa data/ora (un'espressione temporale come ad esempio "1 week 2 days" o una data ISO):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Mostra le differenze tramite delle statistiche come quali file modificati o l'istogramma e il totale delle righe inserite/cancellate:

`git diff --stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Mostra un riepilogo dei file creati, rinominati o la cui modalità è cambiata a partire da un dato commit:

`git diff --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Confronta le versioni di un dato file tra due rami o commit:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo_2</span>` [--] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Confronta le versioni di più file tra il ramo corrente e un altro ramo:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>
