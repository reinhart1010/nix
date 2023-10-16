---
layout: page
title: common/git-rscp (English)
description: "Reverse `git scp` - copy files from the working directory of a remote repository to the current working tree."
content_hash: 7034aced1aefab1817646a94063ea7f8fafb0ec7
last_modified_at: 2023-10-16
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git rscp

Reverse `git scp` - copy files from the working directory of a remote repository to the current working tree.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-scp>.

- Copy specific files from a remote:

`git rscp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Copy a specific directory from a remote:

`git rscp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
