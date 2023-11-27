---
layout: page
title: common/git-write-tree (English)
description: "Low level utility to create a tree object from the current index."
content_hash: c0e050f4892e353a0a4204bbdcec4349dbde3087
last_modified_at: 2023-11-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-write-tree.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git write-tree

Low level utility to create a tree object from the current index.
More information: <https://git-scm.com/docs/git-write-tree>.

- Create a tree object from the current index:

`git write-tree`

- Create a tree object without checking whether objects referenced by the directory exist in the object database:

`git write-tree --missing-ok`

- Create a tree object that represents a subdirectory (used to write the tree object for a subproject in the named subdirectory):

`git write-tree --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdirectory</span>`/`
