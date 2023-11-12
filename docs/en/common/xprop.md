---
layout: page
title: common/xprop (English)
description: "A tool for displaying window and font properties in an X server."
content_hash: 19de8f16b7fe54ec526cd4fb3e017f3b72e054ae
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xprop

A tool for displaying window and font properties in an X server.
More information: <https://manned.org/xprop>.

- Display the name of the root window:

`xprop -root WM_NAME`

- Display the window manager hints for a window:

`xprop -name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">window_name</span>`" WM_HINTS`

- Display the point size of a font:

`xprop -font "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">font_name</span>`" POINT_SIZE`

- Display all the properties of the window with the id 0x200007:

`xprop -id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0x200007</span>
