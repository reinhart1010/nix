---
layout: page
title: common/git-clean (français)
description: "Supprimer les fichiers non-suivis d'un dépôt Git."
content_hash: e2f192aa6de600ff5c968510b168384e3b9834e1
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-clean.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-clean.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-clean.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-clean.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-clean.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clean.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git clean

Supprimer les fichiers non-suivis d'un dépôt Git.
Plus d'informations : <https://git-scm.com/docs/git-clean>.

- Supprimer les fichiers non-suivis :

`git clean`

- Supprimer les fichiers non-suivis de manière interactive :

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>

- Affiche les fichiers non-suivis qui peuvent être supprimés :

`git clean --dry-run`

- Nettoyage forcé des fichiers non-suivis :

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>

- Nettoyage forcé des répertoires non-suivis :

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>` -d`

- Supprime tous les fichiers suivis, incluant ceux répertoriés par `.gitignore` et `.git/info/exclude` :

`git clean -x`
