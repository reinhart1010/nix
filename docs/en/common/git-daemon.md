---
layout: page
title: common/git-daemon (English)
description: "A really simple server for Git repositories."
content_hash: f1dbe7719de6206a343e9e2abe71e6b64aaf6ba7
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git daemon

A really simple server for Git repositories.
More information: <https://git-scm.com/docs/git-daemon>.

- Launch a Git daemon with a whitelisted set of directories:

`git daemon --export-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory2</span>

- Launch a Git daemon with a specific base directory and allow pulling from all sub-directories that look like Git repositories:

`git daemon --base-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --export-all --reuseaddr`

- Launch a Git daemon for the specified directory, verbosely printing log messages and allowing Git clients to write to it:

`git daemon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --enable=receive-pack --informative-errors --verbose`
