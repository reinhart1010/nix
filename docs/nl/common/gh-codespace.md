---
layout: page
title: common/gh-codespace (Nederlands)
description: "Verbind en beheer je codespaces in GitHub."
content_hash: a97be9596788a41410012dd284b612b4fca87e0a
last_modified_at: 2023-12-14
related_topics:
  - title: English version
    url: /en/common/gh-codespace.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-codespace.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh codespace

Verbind en beheer je codespaces in GitHub.
Meer informatie: <https://cli.github.com/manual/gh_codespace>.

- Maak interactief een codespace aan in GitHub:

`gh codespace create`

- Toon alle beschikbare codespaces:

`gh codespace list`

- Verbind interactief met een codespace via SSH:

`gh codespace ssh`

- Kopieer interactief een specifiek bestand naar de codespace:

`gh codespace cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron_file</span>` remote:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/remote_bestand</span>

- Toon interactief de poorten van een codespace:

`gh codespace ports`

- Toon interactief de logs van een codespace:

`gh codespace logs`

- Verwijder interactief een codespace:

`gh codespace delete`

- Toon hulp voor een subcommando:

`gh codespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code|cp|create|delete|edit|...</span>` --help`
