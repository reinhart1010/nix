---
layout: page
title: linux/grim (English)
description: "Grab images (Screenshots) from a Wayland compositor."
content_hash: 08d5339c8068aff6ebae43132349b10055c4e2f7
last_modified_at: 2023-05-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># grim

Grab images (Screenshots) from a Wayland compositor.
More information: <https://sr.ht/~emersion/grim>.

- Screenshot all outputs:

`grim`

- Screenshot a specific output:

`grim -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Screenshot a specific region:

`grim -g "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><x_position>,<y_position> <width>x<height></span>`"`

- Select a specific region and screenshot it, (using slurp):

`grim -g "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$(slurp)</span>`"`

- Use a custom filename:

`grim "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>`"`

- Screenshot and copy to clipboard:

`grim - | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clipboard_manager</span>
