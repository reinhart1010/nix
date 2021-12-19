---
layout: page
title: common/atrm (English)
description: "Remove jobs scheduled by `at` or `batch` commands."
content_hash: ffae537fcf530c75c5e0dcd67f643b248594a489
related_topics:
  - title: italiano version
    url: /it/common/atrm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atrm.html
    icon: bi bi-globe
---
# atrm

Remove jobs scheduled by `at` or `batch` commands.
To find job numbers use `atq`.
More information: <https://man.archlinux.org/man/at.1>.

- Remove job number 10:

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Remove many jobs, separated by spaces:

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>
