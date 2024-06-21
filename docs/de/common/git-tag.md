---
layout: page
title: common/git-tag (Deutsch)
description: "Erstelle, lösche, überprüfe und liste Tags auf."
content_hash: e6f48f3d6a33b34eabeb1f4917ce4bb25e06e572
last_modified_at: 2024-06-21
related_topics:
  - title: English version
    url: /en/common/git-tag.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-tag.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-tag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-tag.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-tag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-tag.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-tag.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git tag

Erstelle, lösche, überprüfe und liste Tags auf.
Weitere Informationen: <https://git-scm.com/docs/git-tag>.

- Liste alle Tags auf:

`git tag`

- Erstelle einen Tag mit Namen, welcher auf den aktuellen Commit zeigt:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>

- Erstelle einen Tag mit Namen, welcher auf einen bestimmten Commit zeigt:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Erstelle einen Tag mit Anmerkung:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anmkerung</span>

- Lösche einen Tag mit bestimmten Namen:

`git tag -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>

- Lade die aktualisierten Tags aus dem Upstream:

`git fetch --tags`

- Liste alle Tags auf, bei denen sich in den vorangegangenen Commits ein bestimmter Commit findet:

`git tag --contains `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
