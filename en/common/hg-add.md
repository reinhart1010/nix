---
layout: page
title: common/hg-add (English)
description: "Adds specified files to the staging area for the next commit in Mercurial."
content_hash: 142887456229c2807aa7f36e85f39110820cbe23
---
# hg add

Adds specified files to the staging area for the next commit in Mercurial.
More information: <https://www.mercurial-scm.org/doc/hg.1.html#add>.

- Add files or directories to the staging area:

`hg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Add all unstaged files matching a specified pattern:

`hg add --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Add all unstaged files, excluding those that match a specified pattern:

`hg add --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Recursively add sub-repositories:

`hg add --subrepos`

- Perform a test-run without performing any actions:

`hg add --dry-run`
