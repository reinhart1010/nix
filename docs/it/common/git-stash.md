---
layout: page
title: common/git-stash (italiano)
description: "Salva in un'area temporanea (stash) modifiche Git locali."
content_hash: 1cc05e26cd2f3dbc5364bffa6b2298b1a82d32b2
last_modified_at: 2023-12-30
related_topics:
  - title: English version
    url: /en/common/git-stash.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-stash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-stash.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-stash.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git stash

Salva in un'area temporanea (stash) modifiche Git locali.
Maggiori informazioni: <https://git-scm.com/docs/git-stash>.

- Salva in un'area temporanea modifiche locali, tranne i file nuovi e non tracciati:

`git stash push -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">messaggio_di_stash_opzionale</span>

- Includi nello stash anche i file nuovi e non tracciati:

`git stash -u`

- Seleziona per lo stash parti di file modificati in modo interattivo:

`git stash -p`

- Elenca tutti gli stash, mostrandone il nome, ramo relativo e messaggio:

`git stash list`

- Applica uno stash (quello predefinito è l'ultimo, chiamato stash@{0}):

`git stash apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_o_commit_stash_opzionale</span>

- Applica uno stash (il predefinito è stash@{0}) e rimuovilo dalla lista degli stash se non ha causato conflitti:

`git stash pop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_stash_opzionale</span>

- Rimuovi tutti gli stash:

`git stash clear`
