---
layout: page
title: common/cb (English)
description: "Cut, copy, and paste anything in the terminal."
content_hash: 9a0a77f2072c8406065c85bfe3cb9163c57821c5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cb

Cut, copy, and paste anything in the terminal.
More information: <https://github.com/Slackadays/Clipboard>.

- Show all clipboards:

`cb`

- Copy a file to the clipboard:

`cb copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Copy some text to the clipboard:

`cb copy "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Some example text</span>`"`

- Copy piped data to the clipboard:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Some example text</span>`" | cb`

- Paste clipboard content:

`cb paste`

- Pipe out clipboard content:

`cb | cat`

- Show clipboard history:

`cb history`

- Show clipboard information:

`cb info`
