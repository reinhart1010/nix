---
layout: page
title: common/git-show-index (English)
description: "Show the packed archive index of a Git repository."
content_hash: 1c9efc12c1caf10b8d1b92f1632986ff885abc9a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git show-index

Show the packed archive index of a Git repository.
More information: <https://git-scm.com/docs/git-show-index>.

- Read an IDX file for a Git packfile and dump its contents to `stdout`:

`git show-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.idx</span>

- Specify the hash algorithm for the index file (experimental):

`git show-index --object-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha1|sha256</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
