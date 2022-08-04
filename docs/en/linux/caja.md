---
layout: page
title: linux/caja (English)
description: "Manages files and directories in MATE desktop environment."
content_hash: 3bb320ec1a721eac0e6714a8ba8d5adc61051120
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># caja

Manages files and directories in MATE desktop environment.
More information: <https://manned.org/caja>.

- Open the current user home directory:

`caja`

- Open specific directories in separate windows:

`caja `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Open specific directories in tabs:

`caja --tabs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Open a directory with a specific window size:

`caja --geometry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">600</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">400</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Close all windows:

`caja --quit`
