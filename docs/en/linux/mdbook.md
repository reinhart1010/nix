---
layout: page
title: linux/mdbook (English)
description: "Create online books by writing Markdown files."
content_hash: c68a0e90cb3eeddc6b6cf44931f757ade52bb362
---
# mdbook

Create online books by writing Markdown files.
More information: <https://rust-lang.github.io/mdBook/>.

- Create a mdbook project in the current directory:

`mdbook init`

- Create a mdbook project in a specific directory:

`mdbook init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Clean the directory with the generated book:

`mdbook clean`

- Serve a book at `http://localhost:3000`, auto build when file changes:

`mdbook serve`

- Watch a set of Markdown files and automatically build when a file is changed:

`mdbook watch`
