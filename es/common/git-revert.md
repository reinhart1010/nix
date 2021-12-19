---
layout: page
title: common/git-revert (español)
description: "Crea nuevos commits que revierten el efecton de los anteriores."
content_hash: 3a5848d2cca9b73c5bc83eb64158d6e41f8f652d
related_topics:
  - title: English version
    url: /en/common/git-revert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-revert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-revert.html
    icon: bi bi-globe
---
# git revert

Crea nuevos commits que revierten el efecton de los anteriores.
Más información: <https://git-scm.com/docs/git-revert>.

- Revierte el commit más reciente:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Revierte el quinto último commit:

`git revert HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Revierte múltiples commits:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama~5..rama~2</span>

- No crea nuevos commits, solo cambia el árbol de trabajo:

`git revert -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0c01a9..9a1743</span>
