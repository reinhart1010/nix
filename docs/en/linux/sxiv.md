---
layout: page
title: linux/sxiv (English)
description: "Simple X Image Viewer."
content_hash: cdb697f2192c84d3341450bf6e19aee578404701
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# sxiv

Simple X Image Viewer.
More information: <https://github.com/muennich/sxiv>.

- Open an image:

`sxiv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Open an image in fullscreen mode:

`sxiv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a newline-separated list of images, reading filenames from `stdin`:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | sxiv -i`

- Open one or more images as a slideshow:

`sxiv -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1 path/to/image2</span>

- Open one or more images in thumbnail mode:

`sxiv -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1 path/to/image2</span>
