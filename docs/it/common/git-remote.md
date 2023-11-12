---
layout: page
title: common/git-remote (italiano)
description: "Gestisci i collegamenti remoti (\"remote\") di un repository locale."
content_hash: f56557ab1e94614706b7d253a94ec2765bac44e0
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-remote.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-remote.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-remote.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-remote.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-remote.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-remote.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-remote.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-remote.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git remote

Gestisci i collegamenti remoti ("remote") di un repository locale.
Maggiori informazioni: <https://git-scm.com/docs/git-remote>.

- Mostra l'elenco dei collegamenti remoti, con il loro nome e URL:

`git remote -v`

- Mostra informazioni su un remote:

`git remote show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remote</span>

- Aggiungi un remote:

`git remote add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_remote</span>

- Modifica l'URL di un remote (usa `--add` per preservare gli URL esistenti):

`git remote set-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuovo_url</span>

- Elimina un remote:

`git remote remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remote</span>

- Rinomina un remote:

`git remote rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vecchio_nome</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuovo_nome</span>
