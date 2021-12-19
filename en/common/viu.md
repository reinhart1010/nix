---
layout: page
title: common/viu (English)
description: "A small command-line application to view images from the terminal."
content_hash: 321ba5b79af53e8ea3b1b3dbf464134c657a00af
---
# viu

A small command-line application to view images from the terminal.
More information: <https://github.com/atanunq/viu>.

- Render an image or animated GIF:

`viu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Render an image or GIF from the internet using `curl`:

`curl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/image.png</span>` | viu -`

- Render an image with a transparent background:

`viu -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Render an image with a specific width and height in pixels:

`viu -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Render an image or GIF and display its file name:

`viu -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
