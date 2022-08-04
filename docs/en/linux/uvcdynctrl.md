---
layout: page
title: linux/uvcdynctrl (English)
description: "A libwebcam command-line tool to manage dynamic controls in uvcvideo."
content_hash: 8a6392975cdc3f1a0cd1cf5e3425a060e06e9eb3
---
# uvcdynctrl

A libwebcam command-line tool to manage dynamic controls in uvcvideo.
More information: <https://manned.org/uvcdynctrl>.

- List all available cameras:

`uvcdynctrl -l`

- Specify the device to use (defaults to `video0`):

`uvcdynctrl -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>

- List available controls:

`uvcdynctrl -c`

- Set a new control value (for negative values, add -- before `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-value</span>`):

`uvcdynctrl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">control_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Get the current control value:

`uvcdynctrl -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">control_name</span>

- Save the state of the current controls to a file:

`uvcdynctrl -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Load the state of the controls from a file:

`uvcdynctrl -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>
