---
layout: page
title: linux/i3-scrot (English)
description: "Wrapper script around the screenshot utility `scrot` for the i3 window manager."
content_hash: bbff403c54ec903312cb11ab61a29991e9284e10
last_modified_at: 2023-06-12
---
# i3-scrot

Wrapper script around the screenshot utility `scrot` for the i3 window manager.
The default save location is `~/Pictures` and can be changed in `~/.config/i3-scrot.conf`.
More information: <https://gitlab.manjaro.org/packages/community/i3/i3-scrot>.

- Capture a screenshot of the whole screen and save it to the default directory:

`i3-scrot`

- Capture a screenshot of the active window:

`i3-scrot --window`

- Capture a screenshot of a specific rectangular selection:

`i3-scrot --select`

- Capture a screenshot of the whole screen and copy it to the clipboard:

`i3-scrot --desk-to-clipboard`

- Capture a screenshot of the active window and copy it to the clipboard:

`i3-scrot --window-to-clipboard`

- Capture a screenshot of a specific selection and copy it to the clipboard:

`i3-scrot --select-to-clipboard`

- Capture a screenshot of the active window after a delay of 5 seconds:

`i3-scrot --window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
