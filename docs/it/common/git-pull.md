---
layout: page
title: common/git-pull (italiano)
description: "Scarica oggetti e riferimenti (fetch) da un repository remoto e avvia un'unione (merge) con il ramo corrente."
content_hash: e1a745b9a6b7ff84ce1af34808d8b620a2f207f1
related_topics:
  - title: Deutsch version
    url: /de/common/git-pull.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-pull.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pull.html
    icon: bi bi-globe
---
# git pull

Scarica oggetti e riferimenti (fetch) da un repository remoto e avvia un'unione (merge) con il ramo corrente.
Maggiori informazioni: <https://git-scm.com/docs/git-pull>.

- Scarica le ultime modifiche dal repository remoto e avvia un'unione:

`git pull`

- Scarica le ultime modifiche dal repository remoto e avvia un rebase:

`git pull --rebase`

- Scarica le ultime modifiche da uno specifico ramo remoto e avvia un'unione con il ramo corrente:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>
