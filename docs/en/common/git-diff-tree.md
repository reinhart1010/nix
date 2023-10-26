---
layout: page
title: common/git-diff-tree (English)
description: "Compares the content and mode of blobs found via two tree objects."
content_hash: 6356e35d903344d6cbc2670ea5ac1faeec85e6cc
last_modified_at: 2023-10-26
---
# git diff-tree

Compares the content and mode of blobs found via two tree objects.
More information: <https://git-scm.com/docs/git-diff-tree>.

- Compare two tree objects:

`git diff-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree-ish1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree-ish2</span>

- Show changes between two specific commits:

`git diff-tree -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit2</span>

- Display changes in patch format:

`git diff-tree -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree-ish1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree-ish2</span>

- Filter changes by a specific path:

`git diff-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree-ish1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree-ish2</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
