---
layout: page
title: common/chsh (Nederlands)
description: "Wijzig de login-shell van de gebruiker."
content_hash: 649cd0883f97302b08155590aacb32b7cb22be28
last_modified_at: 2024-02-05
related_topics:
  - title: bosanski version
    url: /bs/common/chsh.html
    icon: bi bi-globe
  - title: dansk version
    url: /da/common/chsh.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/chsh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chsh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chsh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chsh.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/chsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chsh.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/chsh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chsh.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/chsh.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/chsh.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chsh

Wijzig de login-shell van de gebruiker.
Meer informatie: <https://manned.org/chsh>.

- Stel interactief een specifieke login-shell in voor de huidige gebruiker:

`chsh`

- Stel een specifieke login-[s]hell in voor de huidige gebruiker:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>

- Stel een login-[s]hell in voor een specifieke gebruiker:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Toon [l]ist met beschikbare shells:

`chsh -l`
