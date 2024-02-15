---
layout: page
title: linux/xclip (English)
description: "X11 clipboard manipulation tool, similar to `xsel`."
content_hash: 196837b80067bf9093ddfff88a4a43fcf74fc3a6
last_modified_at: 2024-02-15
related_topics:
  - title: العربية version
    url: /ar/linux/xclip.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/xclip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/xclip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xclip

X11 clipboard manipulation tool, similar to `xsel`.
Handles the X primary and secondary selections, plus the system clipboard (`Ctrl + C`/`Ctrl + V`).
See also: `wl-copy`.
More information: <https://manned.org/xclip>.

- Copy the output from a command to the X11 primary selection area (clipboard):

`echo 123 | xclip`

- Copy the output from a command to a given X11 selection area:

`echo 123 | xclip -selection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primary|secondary|clipboard</span>

- Copy the output from a command to the system clipboard, using short notation:

`echo 123 | xclip -sel clip`

- Copy the contents of a file into the system clipboard:

`xclip -sel clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.txt</span>

- Copy the contents of a PNG into the system clipboard (can be pasted in other programs correctly):

`xclip -sel clip -t image/png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.png</span>

- Copy the user input in the console into the system clipboard:

`xclip -i`

- Paste the contents of the X11 primary selection area to the console:

`xclip -o`

- Paste the contents of the system clipboard to the console:

`xclip -o -sel clip`
