---
layout: page
title: common/git-merge (français)
description: "Pour fusionner des branches `git`."
content_hash: 8e7ac775c40489e8fc45b42fb29c0abc66824c77
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/git-merge.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-merge.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-merge.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-merge.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-merge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git merge

Pour fusionner des branches `git`.
Plus d'informations : <https://git-scm.com/docs/git-merge>.

- Fusionne une branche dans votre branche courante :

`git merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Editer le message de fusion (`merge commit`) :

`git merge --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Fusionner une branche et créer un commit de fusion (`merge commit`) :

`git merge --no-ff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Annuler une fusion en cas de conflit :

`git merge --abort`
