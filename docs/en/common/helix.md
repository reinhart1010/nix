---
layout: page
title: common/helix (English)
description: "Helix, A post-modern text editor, provides several modes for different kinds of text manipulation."
content_hash: ba694623c8784b63e5645bbb0254e3f191000611
last_modified_at: 2024-11-07
related_topics:
  - title: 한국어 version
    url: /ko/common/helix.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/helix.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/helix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# helix

Helix, A post-modern text editor, provides several modes for different kinds of text manipulation.
Pressing `i` enters insert mode. `<Esc>` enters normal mode, which enables the use of Helix commands.
More information: <https://helix-editor.com>.

- Open a file:

`helix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open files and show them one next each other:

`helix --vsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2</span>

- Show the tutorial to learn Helix (or access it within Helix by pressing `<Esc>` and typing `:tutor`):

`helix --tutor`

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
