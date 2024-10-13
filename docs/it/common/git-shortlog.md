---
layout: page
title: common/git-shortlog (italiano)
description: "Riassume l'output di `git log`."
content_hash: 854787f5640c3a8a1fabfb48742daabfb4468158
last_modified_at: 2024-10-13
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
  - title: 한국어 version
    url: /ko/common/git-shortlog.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-shortlog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git shortlog

Riassume l'output di `git log`.
Maggiori informazioni: <https://git-scm.com/docs/git-shortlog>.

- Mostra un riassunto dei commit fatti, raggruppati alfabeticamente per nome dell'autore:

`git shortlog`

- Mostra un riassunto dei commit fatti, ordinati per numero di commit:

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>

- Mostra un riassunto dei commit fatti, raggruppati per identità dell'utente che ha eseguito il commit (nome e email):

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--committer</span>

- Mostra un riassunto degli ultimi 5 commit (richiesti sottoforma di intervallo di revisione):

`git shortlog HEAD~5..HEAD`

- Mostra tutti gli utenti, email e numero di commit nel ramo corrente:

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--summary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--email</span>

- Mostra tutti gli utenti, email e numero di commit in tutti i rami:

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--summary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--email</span>` --all`
