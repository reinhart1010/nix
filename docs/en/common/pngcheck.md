---
layout: page
title: common/pngcheck (English)
description: "Print detailed information about and verify PNG, JNG, and MNG files."
content_hash: 3fde5aee2517710389f6bd28d21d94be98be6cae
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

- Receive an image from stdin and display detailed information:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.png</span>` | pngcheck -cvt`

- [s]earch for PNGs within a specific file and display information about them:

`pngcheck -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>

- Search for PNGs within another file and e[x]tract them:

`pngcheck -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>
