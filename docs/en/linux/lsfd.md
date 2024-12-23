---
layout: page
title: linux/lsfd (English)
description: "List open files and the corresponding processes in Linux."
content_hash: a5eafe8963422dc7ca1107f31a4929ffd01159b5
last_modified_at: 2024-12-23
tldri18n_status: 2
---
# lsfd

List open files and the corresponding processes in Linux.
More information: <https://manned.org/lsfd>.

- List all open file descriptors:

`lsfd`

- List all files kept open by a specific program:

`lsfd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-Q|--filter</span>` 'PID == `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_ID</span>`'`

- Check what program has a specific file open:

`lsfd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-Q|--filter</span>` "NAME == '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>`'"`

- List open IPv4 or IPv6 sockets:

`lsfd -i`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>
