---
layout: page
title: common/git-shortlog (italiano)
description: "Riassume l'output di `git log`."
content_hash: e1cc019da9c301c6ff4b0861fae43a18c28ad75a
related_topics:
  - title: English version
    url: /en/common/git-shortlog.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-shortlog.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-shortlog.html
    icon: bi bi-globe
---
# git shortlog

Riassume l'output di `git log`.
Maggiori informazioni: <https://git-scm.com/docs/git-shortlog>.

- Mostra un riassunto dei commit fatti, raggruppati alfabeticamente per nome dell'autore:

`git shortlog`

- Mostra un riassunto dei commit fatti, ordinati per numero di commit:

`git shortlog -n`

- Mostra un riassunto dei commit fatti, raggruppati per identità dell'utente che ha eseguito il commit (nome e email):

`git shortlog -c`

- Mostra un riassunto degli ultimi 5 commit (richiesti sottoforma di intervallo di revisione):

`git shortlog HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>`..HEAD`

- Mostra tutti gli utenti, email e numero di commit nel ramo corrente:

`git shortlog -sne`

- Mostra tutti gli utenti, email e numero di commit in tutti i rami:

`git shortlog -sne --all`
