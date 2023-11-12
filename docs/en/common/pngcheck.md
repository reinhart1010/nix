---
layout: page
title: common/pngcheck (English)
description: "Print detailed information about and verify PNG, JNG, and MNG files."
content_hash: a435ec9f93b13709d2a572f6c706fb8eac08d3ff
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pngcheck

Print detailed information about and verify PNG, JNG, and MNG files.
More information: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- Print a summary for an image (width, height, and color depth):

`pngcheck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>

- Print information for an image with [c]olorized output:

`pngcheck -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>

- Print [v]erbose information for an image:

`pngcheck -cvt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>

- Receive an image from `stdin` and display detailed information:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.png</span>` | pngcheck -cvt`

- [s]earch for PNGs within a specific file and display information about them:

`pngcheck -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>

- Search for PNGs within another file and e[x]tract them:

`pngcheck -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>
