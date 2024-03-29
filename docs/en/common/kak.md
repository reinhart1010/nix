---
layout: page
title: common/kak (English)
description: "Kakoune is a mode-based code editor implementing the \"multiple selections\" paradigm."
content_hash: 2d008a0e449418fb709259152d7fd0c695804d41
last_modified_at: 2023-12-29
tldri18n_status: 2
---
# kak

Kakoune is a mode-based code editor implementing the "multiple selections" paradigm.
Data can be selected and simultaneously edited in different locations, using multiple selections; users can also connect to the same session for collaborative editing.
More information: <https://kakoune.org>.

- Open a file and enter normal mode, to execute commands:

`kak `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Enter insert mode from normal mode, to write text into the file:

`i`

- Escape insert mode, to go back to normal mode:

`<Esc>`

- Replace all instances of "foo" in the current file with "bar":

`%s`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`<Enter>c`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>`<Esc>`

- Unselect all secondary selections, and keep only the main one:

`<Space>`

- Search for numbers and select the first two:

`/\d+<Enter>N`

- Insert the contents of a file:

`!cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`<Enter>`

- Save the current file:

`:w<Enter>`
