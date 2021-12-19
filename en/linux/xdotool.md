---
layout: page
title: linux/xdotool (English)
description: "Command-line automation for X11."
content_hash: d05b00ee75ffc941dcad333c5a6671638fc2c0d2
---
# xdotool

Command-line automation for X11.

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
