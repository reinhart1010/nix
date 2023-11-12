---
layout: page
title: common/git-stripspace (English)
description: "Read text (e.g. commit messages, notes, tags, and branch descriptions) from `stdin` and clean it into the manner used by Git."
content_hash: 3dc0bf15fb0364d00fd1d0288777d743559c21ed
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/git-stripspace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git stripspace

Read text (e.g. commit messages, notes, tags, and branch descriptions) from `stdin` and clean it into the manner used by Git.
More information: <https://git-scm.com/docs/git-stripspace>.

- Trim whitespace from a file:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | git stripspace`

- Trim whitespace and Git comments from a file:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | git stripspace --strip-comments`

- Convert all lines in a file into Git comments:

`git stripspace --comment-lines < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
