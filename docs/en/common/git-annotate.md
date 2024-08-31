---
layout: page
title: common/git-annotate (English)
description: "Show commit hash and last author on each line of a file."
content_hash: 6601c5d3d39956af4bee80ce4415e1fcf99688bd
last_modified_at: 2024-08-31
related_topics:
  - title: Indonesia version
    url: /id/common/git-annotate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-annotate.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-annotate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git annotate

Show commit hash and last author on each line of a file.
See `git blame`, which is preferred over `git annotate`.
`git annotate` is provided for those familiar with other version control systems.
More information: <https://git-scm.com/docs/git-annotate>.

- Print a file with the author name and commit hash prepended to each line:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print a file with the author [e]mail and commit hash prepended to each line:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--show-email|-e</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print only rows that match a regular expression:

`git annotate -L :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regexp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
