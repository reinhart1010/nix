---
layout: page
title: common/nproc (Nederlands)
description: "Toon het aantal beschikbare verwerkingsunits (meestal CPU's)."
content_hash: c59a9af79a38f3f6a69f583fc8c289ba7b36140f
last_modified_at: 2024-06-27
related_topics:
  - title: English version
    url: /en/common/nproc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nproc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nproc

Toon het aantal beschikbare verwerkingsunits (meestal CPU's).
Meer informatie: <https://www.gnu.org/software/coreutils/nproc>.

- Toon het aantal beschikbare verwerkingsunits:

`nproc`

- Toon het aantal geïnstalleerde verwerkingsunits, inclusief eventuele inactieve:

`nproc --all`

- Trek, indien mogelijk, een bepaald aantal units af van de geretourneerde waarde:

`nproc --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal</span>
