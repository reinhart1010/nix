---
layout: page
title: common/autojump (English)
description: "Quickly jump among the directories you visit the most."
content_hash: 28848b7b210ea8d436a352e207b84d1188389e5d
related_topics:
  - title: italiano version
    url: /it/common/autojump.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autojump.html
    icon: bi bi-globe
---
# autojump

Quickly jump among the directories you visit the most.
Aliases like j or jc are provided for even less typing.
More information: <https://github.com/wting/autojump>.

- Jump to a directory that contains the given pattern:

`j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Jump to a sub-directory (child) of the current directory that contains the given pattern:

`jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Open a directory that contains the given pattern in the operating system file manager:

`jo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Remove non-existing directories from the autojump database:

`j --purge`

- Show the entries in the autojump database:

`j -s`
