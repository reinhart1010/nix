---
layout: page
title: linux/mdbook (English)
description: "Create online books by writing Markdown files."
content_hash: 582492518339cd300bb4e67b234e8c7bbfe23d6e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mdbook

Create online books by writing Markdown files.
More information: <https://rust-lang.github.io/mdBook/>.

- Create an mdbook project in the current directory:

`mdbook init`

- Create an mdbook project in a specific directory:

`mdbook init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Clean the directory with the generated book:

`mdbook clean`

- Serve a book at <http://localhost:3000>, auto build when file changes:

`mdbook serve`

- Watch a set of Markdown files and automatically build when a file is changed:

`mdbook watch`
