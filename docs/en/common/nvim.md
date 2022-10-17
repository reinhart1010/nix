---
layout: page
title: common/nvim (English)
description: "Neovim, a programmer's text editor based on Vim, provides several modes for different kinds of text manipulation."
content_hash: 0035337673041aab8462be99ee2922cbd584e856
related_topics:
  - title: Indonesia version
    url: /id/common/nvim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nvim.html
    icon: bi bi-globe
---
# nvim

Neovim, a programmer's text editor based on Vim, provides several modes for different kinds of text manipulation.
Pressing `i` in normal mode enters insert mode. `<Esc>` goes back to normal mode, which doesn't allow regular text insertion.
More information: <https://neovim.io>.

- Open a file:

`nvim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Enter text editing mode (insert mode):

`<Esc>i`

- Copy ("yank") or cut ("delete") the current line (paste it with `P`):

`<Esc>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yy|dd</span>

- Enter normal mode and undo the last operation:

`<Esc>u`

- Search for a pattern in the file (press `n`/`N` to go to next/previous match):

`<Esc>/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`<Enter>`

- Perform a regular expression substitution in the whole file:

`<Esc>:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>`/g<Enter>`

- Enter normal mode and save (write) the file, and quit:

`<Esc>:wq<Enter>`

- Quit without saving:

`<Esc>:q!<Enter>`
