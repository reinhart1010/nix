---
layout: page
title: common/git-scp (English)
description: "Copy files from the current working tree to the working directory of a remote repository."
content_hash: 64257aa277e3330060b1abda3095fe0690f75cec
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git scp

Copy files from the current working tree to the working directory of a remote repository.
Part of `git-extras`. Uses `rsync` to transfer files.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-scp>.

- Copy unstaged files to a specific remote:

`git scp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Copy staged and unstaged files to a remote:

`git scp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` HEAD`

- Copy files that has been changed in the last commit and any staged or unstaged files to a remote:

`git scp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` HEAD~1`

- Copy specific files to a remote:

`git scp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Copy a specific directory to a remote:

`git scp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
