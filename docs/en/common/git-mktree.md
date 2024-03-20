---
layout: page
title: common/git-mktree (English)
description: "Build a tree object using `ls-tree` formatted text."
content_hash: 6c51d21e4e579f9ee9c9257b4b43ecebe7c536db
last_modified_at: 2024-03-20
tldri18n_status: 2
---
# git mktree

Build a tree object using `ls-tree` formatted text.
More information: <https://git-scm.com/docs/git-mktree>.

- Build a tree object and verify that each tree entry’s hash identifies an existing object:

`git mktree`

- Allow missing objects:

`git mktree --missing`

- Read the NUL ([z]ero character) terminated output of the tree object (`ls-tree -z`):

`git mktree -z`

- Allow the creation of multiple tree objects:

`git mktree --batch`

- Sort and build a tree from `stdin` (non-recursive `git ls-tree` output format is required):

`git mktree < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/tree.txt</span>
