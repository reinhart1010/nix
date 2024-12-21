---
layout: page
title: linux/lsfd (English)
description: "List open files and the corresponding processes in Linux."
content_hash: 9f804452dd3db06dece62313db6bd33a7ea775d7
last_modified_at: 2024-12-21
tldri18n_status: 2
---
# lsfd

List open files and the corresponding processes in Linux.
More information: <https://manned.org/lsfd>.

- List all open file descriptors:

`lsfd`

- List all files kept open by a specific program:

`lsfd -Q 'PID == `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_ID</span>`'`

- Check what program has a specific file open:

`lsfd -Q "NAME == '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>`'"`

- List open IPv4 or IPv6 sockets:

`lsfd -i`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>
