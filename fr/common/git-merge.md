---
layout: page
title: common/git-merge (français)
description: "Pour fusionner des branches `git`."
content_hash: 918e6b5ec0791a5611d1f5bbc3f877b888fd96ab
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
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-merge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git merge

Pour fusionner des branches `git`.
Plus d'informations : <https://git-scm.com/docs/git-merge>.

- Fusionne une branche dans votre branche courante :

`git merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Editer le message de fusion (`merge commit`) :

`git merge -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Fusionner une branche et créer un commit de fusion (`merge commit`) :

`git merge --no-ff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Annuler une fusion en cas de conflit :

`git merge --abort`

- Continuer une fusion après une résolution de conflit :

`git merge --continue`
