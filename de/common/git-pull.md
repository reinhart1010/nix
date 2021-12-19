---
layout: page
title: common/git-pull (Deutsch)
description: "Hole Branches von einem entfernten Repository und binde sie in das lokale Repository ein."
content_hash: 8a714e31955c6540c6dfbe7abd8ff18de782bc1a
related_topics:
  - title: English version
    url: /en/common/git-pull.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pull.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-pull.html
    icon: bi bi-globe
---
# git pull

Hole Branches von einem entfernten Repository und binde sie in das lokale Repository ein.
Weitere Informationen: <https://git-scm.com/docs/git-pull>.

- Lade Änderungen vom Standard-Repository herunter und führe diese zusammen:

`git pull`

- Lade Änderungen vom Standard-Repository herunter und wende einen Rebase an:

`git pull --rebase`

- Lade Änderungen vom Standard-Repository herunter und führe diese in den HEAD zusammen:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>
