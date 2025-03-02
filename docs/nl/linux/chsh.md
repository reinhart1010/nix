---
layout: page
title: linux/chsh (Nederlands)
description: "Verander de login shell van een gebruiker."
content_hash: 8db908ae60fa65abd34a61be6ae78f6c60d3271c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/chsh.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/chsh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/chsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chsh

Verander de login shell van een gebruiker.
Onderdeel van `util-linux`.
Meer informatie: <https://manned.org/chsh>.

- Stel een specifieke login shell interactief in voor de huidige gebruiker:

`chsh`

- Stel een specifieke login[s]hell in voor de huidige gebruiker:

`chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>

- Stel een login[s]hell in voor een specifieke gebruiker:

`sudo chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>
