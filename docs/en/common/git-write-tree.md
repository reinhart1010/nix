---
layout: page
title: common/git-write-tree (English)
description: "Low level utility to create a tree object from the current index."
content_hash: c0e050f4892e353a0a4204bbdcec4349dbde3087
last_modified_at: 2023-11-28
tldri18n_status: 2
---
# git write-tree

Low level utility to create a tree object from the current index.
More information: <https://git-scm.com/docs/git-write-tree>.

- Create a tree object from the current index:

`git write-tree`

- Create a tree object without checking whether objects referenced by the directory exist in the object database:

`git write-tree --missing-ok`

- Create a tree object that represents a subdirectory (used to write the tree object for a subproject in the named subdirectory):

`git write-tree --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdirectory</span>`/`
