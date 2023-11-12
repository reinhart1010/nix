---
layout: page
title: common/atrm (English)
description: "Remove jobs scheduled by `at` or `batch` commands."
content_hash: 7f683b35d44bbaac9408d9fcc8a15d91a161dded
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/atrm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atrm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atrm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atrm

Remove jobs scheduled by `at` or `batch` commands.
To find job numbers use `atq`.
More information: <https://manned.org/atrm>.

- Remove job number 10:

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Remove many jobs, separated by spaces:

`atrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>
