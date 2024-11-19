---
layout: page
title: common/npm-ls (Nederlands)
description: "Print alle geïnstalleerde pakketten naar `stdout`."
content_hash: e8099a3a38ad74d379b993012484939388807c5b
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/npm-ls.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-ls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm ls

Print alle geïnstalleerde pakketten naar `stdout`.
Meer informatie: <https://docs.npmjs.com/cli/commands/npm-ls>.

- Print alle versies van directe afhankelijkheden naar `stdout`:

`npm ls`

- Print alle geïnstalleerde pakketten inclusief gelijkwaardige afhankelijkheden:

`npm ls --all`

- Print afhankelijkheden met uitgebreide informatie:

`npm ls --long`

- Print afhankelijkheden in parseable formaat:

`npm ls --parseable`

- Print afhankelijkheden in JSON formaat:

`npm ls --json`
