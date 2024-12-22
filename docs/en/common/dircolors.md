---
layout: page
title: common/dircolors (English)
description: "Output commands to set the LS_COLOR environment variable and style `ls`, `dir`, etc."
content_hash: dfe3edebeafb8e66dba0a4827f420f4a136000f5
last_modified_at: 2024-12-22
related_topics:
  - title: italiano version
    url: /it/common/dircolors.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dircolors.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/dircolors.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dircolors

Output commands to set the LS_COLOR environment variable and style `ls`, `dir`, etc.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html>.

- Output commands to set LS_COLOR using default colors:

`dircolors`

- Display each filetype with the color they would appear in `ls`:

`dircolors --print-ls-colors`

- Output commands to set LS_COLOR using colors from a file:

`dircolors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Output commands for Bourne shell:

`dircolors --bourne-shell`

- Output commands for C shell:

`dircolors --c-shell`

- View the default colors for file types and extensions:

`dircolors --print-data`
