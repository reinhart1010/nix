---
layout: page
title: common/git-stripspace (English)
description: "Read text (e.g. commit messages, notes, tags, and branch descriptions) from the standard input and clean it into the manner used by Git."
content_hash: e05c30dd7f6bcdc1109ca0a8410d94be34ad04b8
---
# git stripspace

Read text (e.g. commit messages, notes, tags, and branch descriptions) from the standard input and clean it into the manner used by Git.
More information: <https://git-scm.com/docs/git-stripspace>.

- Trim whitespace from a file:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | git stripspace`

- Trim whitespace and Git comments from a file:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | git stripspace --strip-comments`

- Convert all lines in a file into Git comments:

`git stripspace --comment-lines < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
