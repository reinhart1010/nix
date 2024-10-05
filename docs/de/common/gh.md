---
layout: page
title: common/gh (Deutsch)
description: "Arbeite mit GitHub von der Konsole aus."
content_hash: 41c0076623a08d36fbc0ba7c8d389d608c80b90c
last_modified_at: 2024-10-05
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
tldri18n_status: 2
---
# gh

Arbeite mit GitHub von der Konsole aus.
Manche Unterbefehle wie `config` sind separat dokumentiert.
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
