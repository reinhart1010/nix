---
layout: page
title: common/git-revert (español)
description: "Crea nuevas confirmaciones que revierten el efecto de los anteriores."
content_hash: 73e6b64ccf926b8b2ac8b1ceed08d6c3b4ec4eff
last_modified_at: 2024-01-13
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
tldri18n_status: 2
---
# git revert

Crea nuevas confirmaciones que revierten el efecto de los anteriores.
Más información: <https://git-scm.com/docs/git-revert>.

- Revierte la confirmación más reciente:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Revierte la quinta confirmación más reciente:

`git revert HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Revierte una confirmación específica:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0c01a9</span>

- Revierte múltiples confirmaciones:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama~5..rama~2</span>

- Revierte confirmaciones sin crear nuevas confirmaciones:

`git revert -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0c01a9..9a1743</span>
