---
layout: page
title: common/git-switch (Deutsch)
description: "Wechsle zwischen Branches. Verfügbar ab Git Version 2.23+."
content_hash: 34e90bab88eab95e5108761d3a9ad33c8cdfa8d0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-switch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-switch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-switch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-switch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-switch.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-switch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git switch

Wechsle zwischen Branches. Verfügbar ab Git Version 2.23+.
Siehe auch `git checkout`.
Weitere Informationen: <https://git-scm.com/docs/git-switch>.

- Wechsle zu einem existierenden Branch:

`git switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branche_name</span>

- Erstelle einen neuen Branch und wechsele zu diesem:

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Erstelle einen neuen Branch basierend auf einem existierenden Commit und wechsele zu diesem:

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Wechsele zum vorherigen Branch:

`git switch -`

- Wechsele zu einem Branch und aktualisiere alle Submodule entsprechend:

`git switch --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Wechsele zu einem Branch und merge automatisch den aktuellen Branch und alle Änderungen, die nicht committed wurden:

`git switch --merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>
