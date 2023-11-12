---
layout: page
title: common/kitty (English)
description: "A fast, feature-rich, GPU based terminal emulator."
content_hash: bd52a22f0ba643df1f6f542ff4f642f4ebbab1dc
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/kitty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kitty

A fast, feature-rich, GPU based terminal emulator.
More information: <https://sw.kovidgoyal.net/kitty/>.

- Open a new terminal:

`kitty`

- Open a terminal with the specified title for the window:

`kitty --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>`"`

- Start the theme-chooser builtin:

`kitty +kitten themes`

- Display an image in the terminal:

`kitty +kitten icat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Copy the contents of `stdin` to the clipboard:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example</span>` | kitty +kitten clipboard`
