---
layout: page
title: linux/xsetwacom (English)
description: "Command-line tool to change settings for Wacom pen tablets at runtime."
content_hash: 7093d9bd968767fa38bc067de7975efa3a7d5ec5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xsetwacom

Command-line tool to change settings for Wacom pen tablets at runtime.
More information: <https://manned.org/xsetwacom>.

- List all the available Wacom devices. The device name is in the first column:

`xsetwacom list`

- Set Wacom area to specific screen. Get name of the screen with `xrandr`:

`xsetwacom set "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>`" MapToOutput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screen</span>

- Set mode to relative (like a mouse) or absolute (like a pen) mode:

`xsetwacom set "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>`" Mode "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Relative|Absolute</span>`"`

- Rotate the input (useful for tablet-PC when rotating screen) by 0|90|180|270 degrees from "natural" rotation:

`xsetwacom set "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>`" Rotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|half|cw|ccw</span>

- Set button to only work when the tip of the pen is touching the tablet:

`xsetwacom set "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>`" TabletPCButton "on"`
