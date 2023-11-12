---
layout: page
title: common/git-fetch (Deutsch)
description: "Lade Objekte und Referenzen (refs) von einem entfernten Repository."
content_hash: 9b993b2c9d1ec51900d128c275b2a8b564032287
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-fetch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-fetch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-fetch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-fetch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-fetch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git fetch

Lade Objekte und Referenzen (refs) von einem entfernten Repository.
Weitere Informationen: <https://git-scm.com/docs/git-fetch>.

- Hole die neuesten Änderungen von dem standardmäßigen Repository im Upstream (wenn gesetzt):

`git fetch`

- Hole neue Branches von einem bestimmten Repository im Upstream:

`git fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_des_upstream_repository</span>

- Hole die neuesten Änderungen von allen Repositories im Upstream:

`git fetch --all`

- Lade auch die Tags des Repository im Upstream:

`git fetch --tags`

- Lösche lokale Referenzen auf entfernte Branches, die im Upstream-Repository nicht mehr existieren:

`git fetch --prune`
