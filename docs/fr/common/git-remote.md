---
layout: page
title: common/git-remote (français)
description: "Organisation des dépôts suivis (\"remotes\")."
content_hash: b78cae414062ed83ab7ab7804b0238370e8ffb39
last_modified_at: 2024-10-13
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
  - title: Indonesia version
    url: /id/common/git-remote.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-remote.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-remote.html
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

Organisation des dépôts suivis ("remotes").
Plus d'informations : <https://git-scm.com/docs/git-remote>.

- Affiche les dépôts existants, leur nom et URL :

`git remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>

- Affiche les informations à propos d'un dépôt :

`git remote show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>

- Ajoute un dépôt :

`git remote add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_distant</span>

- Change l'URL d'un dépôt (ajouter `--add` pour conserver l'URL existante) :

`git remote set-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_url</span>

- Supprime un dépôt :

`git remote remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>

- Renomme un dépôt :

`git remote rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_name</span>
