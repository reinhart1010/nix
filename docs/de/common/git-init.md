---
layout: page
title: common/git-init (Deutsch)
description: "Erstelle eine neues lokales Git-Repository."
content_hash: c8236dd670ca43a8911f899c3ca41ff4e607f027
related_topics:
  - title: English version
    url: /en/common/git-init.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-init.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-init.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/git-init.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-init.html
    icon: bi bi-globe
---
# git init

Erstelle eine neues lokales Git-Repository.
Weitere Informationen: <https://git-scm.com/docs/git-init>.

- Erstelle eine neues lokales Repository:

`git init`

- Erstelle eine neues Repository mit einem bestimmten Namen für den ersten Branch:

`git init --initial-branch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Erstelle ein neues Repository, welches SHA256 für Objekt-Hashes verwendet (benötigt Git 2.29+):

`git init --object-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha256</span>

- Erstelle eine neues minimales Repository, welches sich für die Verwendung als Remote-Repository über SSH eignet:

`git init --bare`
