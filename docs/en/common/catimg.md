---
layout: page
title: common/catimg (English)
description: "Image printing in the terminal."
content_hash: 6db69530c8ee29ce182dcbc14aeace64b9b36746
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# catimg

Image printing in the terminal.
See also: `pixterm`, `chafa`.
More information: <https://github.com/posva/catimg>.

- Print a JPEG, PNG, or GIF to the terminal:

`catimg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Double the [r]esolution of an image:

`catimg -r 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Disable 24-bit color for better [t]erminal support:

`catimg -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Specify a custom [w]idth or [H]eight:

`catimg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-w|-H</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
