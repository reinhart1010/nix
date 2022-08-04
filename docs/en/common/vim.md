---
layout: page
title: common/vim (English)
description: "Vim (Vi IMproved), a command-line text editor, provides several modes for different kinds of text manipulation."
content_hash: 918eca4ef71be3cc1deb2e17cebf3f8ede5fe51a
related_topics:
  - title: Deutsch version
    url: /de/common/vim.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vim.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/vim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/vim.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/vim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vim.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/vim.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/vim.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/vim.html
    icon: bi bi-globe
---
# vim

Vim (Vi IMproved), a command-line text editor, provides several modes for different kinds of text manipulation.
Pressing `i` enters insert mode. `<Esc>` enters normal mode, which enables the use of Vim commands.
More information: <https://www.vim.org>.

- Open a file:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a file at a specified line number:

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- View Vim's help manual:

`:help<Enter>`

- Save and Quit:

`:wq<Enter>`

- Undo the last operation:

`u`

- Search for a pattern in the file (press `n`/`N` to go to next/previous match):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`<Enter>`

- Perform a regular expression substitution in the whole file:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>`/g<Enter>`

- Display the line numbers:

`:set nu<Enter>`
