---
layout: page
title: common/chsh (Deutsch)
description: "Ändere die Login-Shell eines Benutzers."
content_hash: 4c0b8811e71d32ccf5e4f243091caf962e6e4cd1
last_modified_at: 2024-02-05
related_topics:
  - title: bosanski version
    url: /bs/common/chsh.html
    icon: bi bi-globe
  - title: dansk version
    url: /da/common/chsh.html
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
  - title: Nederlands version
    url: /nl/common/chsh.html
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

Ändere die Login-Shell eines Benutzers.
Weitere Informationen: <https://manned.org/chsh>.

- Ändere die Login-Shell des aktuellen Benutzers interaktiv:

`chsh`

- Ändere die Login-Shell des aktuellen Benutzers:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/shell</span>

- Ändere die Login-Shell eines Benutzers:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>

- Liste alle verfügbaren Shells auf:

`chsh -l`
