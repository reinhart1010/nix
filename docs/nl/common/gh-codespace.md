---
layout: page
title: common/gh-codespace (Nederlands)
description: "Verbind en beheer je codespaces in GitHub."
content_hash: b584c52f57435ebdfc4cf11bea69b401ae6ce313
last_modified_at: 2024-02-01
related_topics:
  - title: English version
    url: /en/common/gh-codespace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh codespace

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

- Toon de help voor een subcommando:

`gh codespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code|cp|create|delete|edit|...</span>` --help`
