---
layout: page
title: linux/wtype (English)
description: "Simulate keyboard input on Wayland, similar to `xdotool type` for X11."
content_hash: fa5668e65ec9e1a77b16858c5481e0c83a8116a6
last_modified_at: 2024-10-10
tldri18n_status: 2
---
# wtype

Simulate keyboard input on Wayland, similar to `xdotool type` for X11.
See also: `ydotool`.
More information: <https://github.com/atx/wtype>.

- Simulate typing text:

`wtype "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- Type a specific key:

`wtype -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Left</span>

- Press a modifier:

`wtype -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shift|ctrl|...</span>

- Release a modifier:

`wtype -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ctrl</span>

- Wait between keystrokes (in milliseconds):

`wtype -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` -- "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>`"`

- Read text from `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>`" | wtype -`
