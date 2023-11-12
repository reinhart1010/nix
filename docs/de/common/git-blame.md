---
layout: page
title: common/git-blame (Deutsch)
description: "Zeige den Commit-Hash und den letzten Autor jeder Zeile einer Datei."
content_hash: fc9f797d6f9c242299ed082fd19535a3c2d68d29
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-blame.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-blame.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-blame.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-blame.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-blame.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-blame.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-blame.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git blame

Zeige den Commit-Hash und den letzten Autor jeder Zeile einer Datei.
Weitere Informationen: <https://git-scm.com/docs/git-blame>.

- Gib die Commit-Hashes und dem Autor jeder Zeile einer Datei aus:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Gib die Commit-Hashes und dem Autor (inklusive E-Mail) jeder Zeile einer Datei aus:

`git blame -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>
