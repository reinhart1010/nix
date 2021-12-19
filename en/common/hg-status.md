---
layout: page
title: common/hg-status (English)
description: "Show files that have changed in the working directory."
content_hash: 93bd33b8fa533068e7fe695b41affddbd297d8c2
---
# hg status

Show files that have changed in the working directory.
More information: <https://www.mercurial-scm.org/doc/hg.1.html#status>.

- Display the status of changed files:

`hg status`

- Display only modified files:

`hg status --modified`

- Display only added files:

`hg status --added`

- Display only removed files:

`hg status --removed`

- Display only deleted (but tracked) files:

`hg status --deleted`

- Display changes in the working directory compared to a specified changeset:

`hg status --rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>

- Display only files matching a specified glob pattern:

`hg status --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Display files, excluding those that match a specified glob pattern:

`hg status --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>
