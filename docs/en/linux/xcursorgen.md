---
layout: page
title: linux/xcursorgen (English)
description: "Create an X cursor file from a collection of PNGs."
content_hash: 3a9ec7ccdcd6e1c35d04059945b93f7a5d9aff3f
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# xcursorgen

Create an X cursor file from a collection of PNGs.
If `--prefix` is omitted, the image files must be located in the current working directory.
More information: <https://manned.org/xcursorgen>.

- Create an X cursor file using a configuration file:

`xcursorgen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.cursor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Create an X cursor file using a configuration file and specify the path to the image files:

`xcursorgen --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_directory/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.cursor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Create an X cursor file using a configuration file and write the output to `stdout`:

`xcursorgen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.cursor</span>
