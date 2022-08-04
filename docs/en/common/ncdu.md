---
layout: page
title: common/ncdu (English)
description: "Disk usage analyzer with an ncurses interface."
content_hash: 50d3f3767cf91146480560b83514905f2aab7924
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ncdu

Disk usage analyzer with an ncurses interface.
More information: <https://manned.org/ncdu>.

- Analyze the current working directory:

`ncdu`

- Colorize output:

`ncdu --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dark|off</span>

- Analyze a given directory:

`ncdu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Save results to a file:

`ncdu -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Exclude files that match a pattern, argument can be given multiple times to add more patterns:

`ncdu --exclude '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`'`
