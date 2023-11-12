---
layout: page
title: linux/xterm (English)
description: "A terminal emulator for the X Window System."
content_hash: 54546a64f18b00492423c05d4b8852488aae183a
last_modified_at: 2023-11-12
related_topics:
  - title: Indonesia version
    url: /id/linux/xterm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/xterm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xterm

A terminal emulator for the X Window System.
More information: <https://manned.org/xterm>.

- Open the terminal with a title of `Example`:

`xterm -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Example</span>

- Open the terminal in fullscreen mode:

`xterm -fullscreen`

- Open the terminal with a dark blue background and yellow foreground (font color):

`xterm -bg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">darkblue</span>` -fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yellow</span>

- Open the terminal with 100 characters per line and 35 lines, in screen position x=200px, y=20px:

`xterm -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">35</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Open the terminal using a Serif font and a font size equal to 20:

`xterm -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Serif'</span>` -fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>
