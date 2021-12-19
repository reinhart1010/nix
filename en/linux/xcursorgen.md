---
layout: page
title: linux/xcursorgen (English)
description: "Create an X cursor file from a collection of PNGs."
content_hash: a029b28403b35e6cbcece959be19d109e8586630
---
# xcursorgen

Create an X cursor file from a collection of PNGs.
If `--prefix` is omitted, the image files must be located in the current working directory.
More information: <https://manned.org/xcursorgen>.

- Create an X cursor file using a config file:

`xcursorgen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.cursor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Create an X cursor file using a config file and specify the path to the image files:

`xcursorgen --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_directory/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.cursor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Create an X cursor file using a config file and write the output to stdout:

`xcursorgen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.cursor</span>
