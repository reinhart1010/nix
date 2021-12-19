---
layout: page
title: common/helix (English)
description: "Helix, A post-modern text editor, provides several modes for different kinds of text manipulation."
content_hash: 80d064b95d929c2740a963cc045d7670f0e86bd0
---
# vim

Helix, A post-modern text editor, provides several modes for different kinds of text manipulation.
Pressing `i` enters insert mode. `<Esc>` enters normal mode, which enables the use of Helix commands.
More information: <https://helix-editor.com/>.

- Open a file:

`helix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Change the Helix theme:

`:theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">theme_name</span>

- Save and Quit:

`:wq<Enter>`

- Force-quit without saving:

`:q!<Enter>`

- Undo the last operation:

`u`

- Search for a pattern in the file (press `n`/`N` to go to next/previous match):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`<Enter>`

- Format the file:

`:format`
