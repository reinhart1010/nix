---
layout: page
title: linux/xcursorgen (English)
description: "Create an X cursor file from a collection of PNGs."
content_hash: 16406b7d5b7ae5e5f127d0fb6e55163c8629dd48
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xcursorgen

Create an X cursor file from a collection of PNGs.
If `--prefix` is omitted, the image files must be located in the current working directory.
More information: <https://manned.org/xcursorgen>.

- Create an X cursor file using a config file:

`xcursorgen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.cursor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Create an X cursor file using a config file and specify the path to the image files:

`xcursorgen --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_directory/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.cursor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Create an X cursor file using a config file and write the output to `stdout`:

`xcursorgen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.cursor</span>
