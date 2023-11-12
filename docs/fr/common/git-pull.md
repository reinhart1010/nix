---
layout: page
title: common/git-pull (français)
description: "Récupère une branche depuis le serveur distant et la fusionne dans la branche local."
content_hash: 053e7ccd0666c490ed0a4837465355ab49d42fdb
last_modified_at: 2023-11-12
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
  - title: Indonesia version
    url: /id/common/git-pull.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-pull.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-pull.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-pull.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-pull.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-pull.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git pull

Récupère une branche depuis le serveur distant et la fusionne dans la branche local.
Plus d'informations : <https://git-scm.com/docs/git-pull>.

- Télécharge les changements depuis le serveur distant par défaut et fusionne les :

`git pull`

- Télécharge les changements depuis le serveur distant par défaut et applique les changements locaux par dessus :

`git pull --rebase`

- Télécharge les changements depuis un serveur et une branche distante, puis fusionne les dans HEAD :

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branche</span>
