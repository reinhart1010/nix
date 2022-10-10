---
layout: page
title: common/gh (Deutsch)
description: "Arbeite mit GitHub von der Konsole aus."
content_hash: 73c98c32a766df4b4275df0297b7ce2aae84d144
related_topics:
  - title: English version
    url: /en/common/gh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/gh.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/gh.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gh

Arbeite mit GitHub von der Konsole aus.
Manche Unterbefehle wie `gh config` sind separat dokumentiert.
Weitere Informationen: <https://cli.github.com/>.

- Klone ein GitHub Repository lokal:

`gh repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">besitzer</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Erstelle ein neues Issue:

`gh issue create`

- Zeige und filter offene Issues des aktuellen Repositories:

`gh issue list`

- Öffne ein Issue im Standard-Webbrowser:

`gh issue view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_nummer</span>

- Erstelle eine Pull Request:

`gh pr create`

- Öffne eine Pull Request im Standard-Webbrowser:

`gh pr view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_nummer</span>

- Wechsle lokal zu einer bestimmten Pull Request:

`gh pr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_nummer</span>

- Zeige den Status der Pull Requests eines Repositories:

`gh pr status`
