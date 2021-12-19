---
layout: page
title: linux/ncdu (English)
description: "Disk usage analyzer with an ncurses interface."
content_hash: f4fabbae3ddf584a03b35bf4e7df19c2ce0938e0
---
# ncdu

Disk usage analyzer with an ncurses interface.

- Analyze the current working directory:

`ncdu`

- Analyze a given directory:

`ncdu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Save results to a file:

`ncdu -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Exclude files that match a pattern, argument can be given multiple times to add more patterns:

`ncdu --exclude '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`'`
