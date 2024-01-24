---
layout: page
title: linux/uvcdynctrl (English)
description: "A libwebcam command-line tool to manage dynamic controls in uvcvideo."
content_hash: 08b69a4da2a3b56c63a449b1af868aefde7758c0
last_modified_at: 2024-01-24
tldri18n_status: 2
---
# uvcdynctrl

A libwebcam command-line tool to manage dynamic controls in uvcvideo.
More information: <https://manned.org/uvcdynctrl>.

- List all available cameras:

`uvcdynctrl -l`

- Use a specific device (defaults to `video0`):

`uvcdynctrl -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>

- List available controls:

`uvcdynctrl -c`

- Set a new control value (for negative values, use `-- -value`):

`uvcdynctrl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">control_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Get the current control value:

`uvcdynctrl -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">control_name</span>

- Save the state of the current controls to a file:

`uvcdynctrl -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Load the state of the controls from a file:

`uvcdynctrl -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>
