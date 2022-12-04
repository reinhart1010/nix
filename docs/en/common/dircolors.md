---
layout: page
title: common/dircolors (English)
description: "Output commands to set the LS_COLOR environment variable and style `ls`, `dir`, etc."
content_hash: 330e1be2c2d0f4923337f3b4f26ae5fb24c0f222
last_modified_at: 2022-12-04
related_topics:
  - title: italiano version
    url: /it/common/dircolors.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dircolors.html
    icon: bi bi-globe
---
# dircolors

Output commands to set the LS_COLOR environment variable and style `ls`, `dir`, etc.
More information: <https://www.gnu.org/software/coreutils/dircolors>.

- Output commands to set LS_COLOR using default colors:

`dircolors`

- Output commands to set LS_COLOR using colors from a file:

`dircolors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Output commands for Bourne shell:

`dircolors --bourne-shell`

- Output commands for C shell:

`dircolors --c-shell`

- View the default colors for file types and extensions:

`dircolors --print-data`
