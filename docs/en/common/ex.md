---
layout: page
title: common/ex (English)
description: "Command-line text editor."
content_hash: 5bf969fb8e1ad80d8bcd5d1dff99058ff2233b11
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ex

Command-line text editor.
See also: `vim`.
More information: <https://www.vim.org>.

- Open a file:

`ex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Save and Quit:

`wq<Enter>`

- Undo the last operation:

`undo<Enter>`

- Search for a pattern in the file:

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`<Enter>`

- Perform a regular expression substitution in the whole file:

`%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>`/g<Enter>`

- Insert text:

`i<Enter>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>`<C-c>`

- Switch to Vim:

`visual<Enter>`
