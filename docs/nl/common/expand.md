---
layout: page
title: common/expand (Nederlands)
description: "Vervang tabs met spaties."
content_hash: 5319dde4e6820e8108ae95dc616816972d3ece20
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/common/expand.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/expand.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/expand.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># expand

Vervang tabs met spaties.
Meer informatie: <https://www.gnu.org/software/coreutils/expand>.

- Vervang tabs in ieder bestand met spaties en schrijf het naar `stdout`:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Vervang tabs met spaties, lezend vanaf `stdin`:

`expand`

- Vervang geen tabs na een karakter:

`expand -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Laat tabs een bepaald aantal tekens uit elkaar staan, niet 8:

`expand -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Gebruik een door komma's gescheiden lijst met expliciete tabposities:

`expand -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,4,6</span>
