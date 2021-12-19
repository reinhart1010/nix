---
layout: page
title: linux/maim (English)
description: "Screenshot utility."
content_hash: 49644ebf30b02bcd8120a6dbe9064b1533585f02
---
# maim

Screenshot utility.
More information: <https://github.com/naelstrof/maim>.

- Capture a screenshot and save it to the given path:

`maim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/screenshot.png</span>

- Capture a screenshot of the selected region:

`maim --select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/screenshot.png</span>

- Capture a screenshot of the selected region and save it in the clipboard (requires `xclip`):

`maim --select | xclip -selection clipboard -target image/png`

- Capture a screenshot of the current active window (requires `xdotool`):

`maim --window $(xdotool getactivewindow) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/screenshot.png</span>
