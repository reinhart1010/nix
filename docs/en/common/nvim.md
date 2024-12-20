---
layout: page
title: common/nvim (English)
description: "Neovim, a programmer's text editor based on Vim, provides several modes for different kinds of text manipulation."
content_hash: efb6025d5452d5adff0501b1f81da58642463393
last_modified_at: 2024-10-21
related_topics:
  - title: Indonesia version
    url: /id/common/nvim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nvim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nvim.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/nvim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvim

Neovim, a programmer's text editor based on Vim, provides several modes for different kinds of text manipulation.
Pressing `i` in normal mode enters insert mode. `<Esc>` goes back to normal mode, which doesn't allow regular text insertion.
See also: `vim`, `vimtutor`, `vimdiff`.
More information: <https://neovim.io>.

- Open a file:

`nvim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

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

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><Esc>ZZ|<Esc>:x<Enter>|<Esc>:wq<Enter></span>

- Quit without saving:

`<Esc>:q!<Enter>`
