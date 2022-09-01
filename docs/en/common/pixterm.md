---
layout: page
title: common/pixterm (English)
description: "Image printing in the terminal."
content_hash: f9cf49db3fc037bb0c8024f1c164bcb7dfb72b8f
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pixterm

Image printing in the terminal.
See also: `chafa`, `catimg`.
More information: <https://github.com/eliukblau/pixterm>.

- Render a static image directly in the terminal:

`pixterm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Use the image's original aspect ratio:

`pixterm -s 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Specify a custom aspect ratio using a specific number of [t]erminal [r]ows and [c]olumns:

`pixterm -tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>` -tc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Filter the output with a [m]atte background color and character [d]ithering:

`pixterm -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">000000</span>` -d 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
