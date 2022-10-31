---
layout: page
title: common/git-merge-repo (English)
description: "Merge two repository histories."
content_hash: 9ab21268ab463786631433abb1383671c11a5950
---
# git merge-repo

Merge two repository histories.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-merge-repo>.

- Merge a repository's branch into the current repository's directory:

`git merge-repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Merge a remote repository's branch into the current repository's directory, not preserving history:

`git merge-repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/remote_repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>` .`
