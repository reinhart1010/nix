---
layout: page
title: linux/wl-paste (English)
description: "Tool to access data stored in the clipboard for Wayland."
content_hash: c5806197989883e27b2fa759bdf44c79b4197932
---
# wl-paste

Tool to access data stored in the clipboard for Wayland.
See also: `wl-copy`.
More information: <https://github.com/bugaevc/wl-clipboard>.

- Paste the contents of the clipboard:

`wl-paste`

- Paste the contents of the clipboard and then clear it:

`wl-paste --paste-once`

- Write the contents of the clipboard to a file:

`wl-paste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Pipe the contents of the clipboard to a command:

`wl-paste | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Clear the clipboard:

`wl-paste --clear`
