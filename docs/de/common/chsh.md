---
layout: page
title: common/chsh (Deutsch)
description: "Ändere die Login-Shell eines Benutzers."
content_hash: 2925a5c7c96e683d10858c731352ef1facbeb90f
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
  - title: हिन्दी version
    url: /hi/common/chsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chsh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chsh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chsh.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
    url: /no/common/chsh.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/chsh.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/chsh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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

`chsh --list-shells`
