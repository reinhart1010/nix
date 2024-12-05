---
layout: page
title: common/rich (English)
description: "A toolbox for fancy output in the terminal."
content_hash: 1abf1dfd382dc292bd6595afccbd46a0867e81e0
last_modified_at: 2024-12-05
related_topics:
  - title: 한국어 version
    url: /ko/common/rich.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rich

A toolbox for fancy output in the terminal.
More information: <https://github.com/Textualize/rich-cli>.

- Display a file with syntax highlighting:

`rich `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Add line numbers, and indentation guides:

`rich `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>` --line-numbers --guides`

- Apply a theme:

`rich `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>` --theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monokai</span>

- Display a file in an interactive pager:

`rich `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>` --pager`

- Display contents from a URL:

`rich `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://raw.githubusercontent.com/Textualize/rich-cli/main/README.md</span>` --markdown --pager`

- Export a file as HTML:

`rich `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md</span>` --export-html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.html</span>

- Display text with formatting tags, custom alignment, and line width:

`rich --print "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello [green on black]Stylized[/green on black] [bold]World[/bold]</span>`" --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">left|center|right</span>` --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
