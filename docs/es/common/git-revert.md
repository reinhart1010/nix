---
layout: page
title: common/git-revert (español)
description: "Crea nuevos commits que revierten el efecto de los anteriores."
content_hash: fce5aec8adbdc7ae07e8982bae663a6931714e53
last_modified_at: 2024-01-07
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
  - title: Türkçe version
    url: /tr/common/git-revert.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git revert

Crea nuevos commits que revierten el efecto de los anteriores.
Más información: <https://git-scm.com/docs/git-revert>.

- Revierte el commit más reciente:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Revierte el quinto último commit:

`git revert HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Revierte múltiples commits:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama~5..rama~2</span>

- Revierte commits sin crear nuevos commits:

`git revert -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0c01a9..9a1743</span>
