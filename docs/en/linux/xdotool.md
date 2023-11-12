---
layout: page
title: linux/xdotool (English)
description: "Command-line automation for X11."
content_hash: 66ab0eabc03914b408d02507065d3d5ae719a7c8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xdotool

Command-line automation for X11.
More information: <https://manned.org/xdotool>.

- Retrieve the X-Windows window ID of the running Firefox window(s):

`xdotool search --onlyvisible --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- Click the right mouse button:

`xdotool click `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Get the ID of the currently active window:

`xdotool getactivewindow`

- Focus on the window with ID of 12345:

`xdotool windowfocus --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12345</span>

- Type a message, with a 500ms delay for each letter:

`xdotool type --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` "Hello world"`

- Press the enter key:

`xdotool key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">KP_Enter</span>
