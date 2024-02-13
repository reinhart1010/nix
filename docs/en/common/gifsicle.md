---
layout: page
title: common/gifsicle (English)
description: "Create, edit, manipulate, and get information about GIF files."
content_hash: 119d8bffd01930c7f7380845582b4062fbea5872
last_modified_at: 2024-02-13
tldri18n_status: 2
---
# gifsicle

Create, edit, manipulate, and get information about GIF files.
More information: <https://www.lcdf.org/gifsicle>.

- Optimize a GIF as a new file:

`gifsicle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gif</span>` --optimize=3 -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gif</span>

- Use [b]atch mode (modify each given file in place) and unoptimize a GIF:

`gifsicle -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gif</span>` --unoptimize`

- Extract a frame from a GIF:

`gifsicle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gif</span>` '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>`' > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/first_frame.gif</span>

- Make a GIF animation from selected GIFs:

`gifsicle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.gif</span>` --delay=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --loop > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gif</span>

- Reduce file size using lossy compression:

`gifsicle -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gif</span>` --optimize=3 --lossy=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --colors=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>` --dither`

- Delete the first 10 frames and all frames after frame 20 from a GIF:

`gifsicle -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gif</span>` --delete '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0-9</span>`' '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20-</span>`'`

- Modify all frames by cropping them to a rectangle, changing their scale, flipping them, and rotating them:

`gifsicle -b --crop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">starting_x</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">starting_y</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rect_width</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rect_height</span>` --scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.25</span>` --flip-horizontal --rotate-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90|180|270</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gif</span>
