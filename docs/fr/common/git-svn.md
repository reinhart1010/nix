---
layout: page
title: common/git-svn (français)
description: "Opération bidirectionnelle entre un référentiel Subversion et Git."
content_hash: f0eb6276052d9bfd9525853a91e445d04f53d5c5
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-svn.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-svn.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-svn.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-svn.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-svn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git svn

Opération bidirectionnelle entre un référentiel Subversion et Git.
Plus d'informations : <https://git-scm.com/docs/git-svn>.

- Cloner un dépôt SVN :

`git svn clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/subversion_repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_dir</span>

- Cloner un dépôt SVN à partir d'une révision donnée :

`git svn clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--revision</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>`:HEAD `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://svn.example.net/subversion/repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_dir</span>

- Mettre à jour le clone local à partir du dépôt SVN distant :

`git svn rebase`

- Chercher les changements distants dans le dépôt SVN dans les appliquer sur le HEAD :

`git svn fetch`

- Commiter sur le SVN :

`git svn commit`
