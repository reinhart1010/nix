---
layout: page
title: linux/scrot (English)
description: "Screen capture utility."
content_hash: 87cb798ff7a654c715a0e283020512dba0951a3d
last_modified_at: 2023-12-16
tldri18n_status: 2
---
# scrot

Screen capture utility.
More information: <https://github.com/resurrecting-open-source-projects/scrot>.

- Capture a screenshot and save it to the current directory with the current date as the filename:

`scrot`

- Capture a screenshot and save it as `capture.png`:

`scrot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">capture.png</span>

- Capture a screenshot interactively:

`scrot --select`

- Capture a screenshot interactively without exiting on keyboard input, press `ESC` to exit:

`scrot --select --ignorekeyboard`

- Capture a screenshot interactively delimiting the region with a colored line:

`scrot --select --line color=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11_color|rgb_color</span>

- Capture a screenshot from the currently focused window:

`scrot --focused`

- Display a countdown of 10 seconds before taking a screenshot:

`scrot --count --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
