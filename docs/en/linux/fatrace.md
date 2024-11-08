---
layout: page
title: linux/fatrace (English)
description: "Report file access events."
content_hash: b44bd61cd16acd47e147d80c6369c67b5ebfdda9
last_modified_at: 2024-11-08
tldri18n_status: 2
---
# fatrace

Report file access events.
More information: <https://manned.org/fatrace>.

- Print file access events in all mounted filesystems to `stdout`:

`sudo fatrace`

- Print file access events on the mount of the current directory, with timestamps, to `stdout`:

`sudo fatrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--current-mount</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--timestamp</span>
