---
layout: page
title: common/ipcs (English)
description: "Show information about the usage of XSI IPC facilities: shared memory segments, message queues, and semaphore arrays."
content_hash: 6de8720caff8c2778d8e7acbf3c76084f197f07d
last_modified_at: 2024-05-07
tldri18n_status: 2
---
# ipcs

Show information about the usage of XSI IPC facilities: shared memory segments, message queues, and semaphore arrays.
More information: <https://manned.org/ipcs.1p>.

- Show information about all the IPC:

`ipcs -a`

- Show information about active shared [m]emory segments, message [q]ueues or [s]empahore sets:

`ipcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|-q|-s</span>

- Show information on maximum allowable size in [b]ytes:

`ipcs -b`

- Show [c]reator’s user name and group name for all IPC facilities:

`ipcs -c`

- Show the [p]ID of the last operators for all IPC facilities:

`ipcs -p`

- Show access [t]imes for all IPC facilities:

`ipcs -t`

- Show [o]utstanding usage for active message queues, and shared memory segments:

`ipcs -o`
