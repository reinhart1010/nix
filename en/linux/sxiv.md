---
layout: page
title: linux/sxiv (English)
description: "Simple X Image Viewer."
content_hash: 3b5669ed08571cff5346c86facac2d5fbb8fd728
---
# sxiv

Simple X Image Viewer.
More information: <https://github.com/muennich/sxiv>.

- Open an image:

`sxiv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open an image in fullscreen mode:

`sxiv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a newline-separated list of images, reading filenames from standard input:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | sxiv -i`

- Open a space-separated list of images as a slideshow:

`sxiv -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a space-separated list of images in thumbnail mode:

`sxiv -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
