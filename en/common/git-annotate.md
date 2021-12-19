---
layout: page
title: common/git-annotate (English)
description: "Show commit hash and last author on each line of a file."
content_hash: 7731f4b2157d93fd25806bd1d9879203927ed858
---
# git annotate

Show commit hash and last author on each line of a file.
See `git blame`, which is preferred over `git annotate`.
`git annotate` is provided for those familiar with other version control systems.
More information: <https://git-scm.com/docs/git-annotate>.

- Print a file with the author name and commit hash prepended to each line:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print a file with the author email and commit hash prepended to each line:

`git annotate -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
