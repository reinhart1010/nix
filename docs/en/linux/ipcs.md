---
layout: page
title: linux/ipcs (English)
description: "Show information about the usage of System V IPC facilities: shared memory segments, message queues, and semaphore arrays."
content_hash: 0bda6f91b528cac544f67787d5d4a5e58399979a
last_modified_at: 2024-05-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ipcs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ipcs

Show information about the usage of System V IPC facilities: shared memory segments, message queues, and semaphore arrays.
See also: `lsipc` for a more flexible tool, `ipcmk` for creating IPC facilities, and `ipcrm` for deleting them.
More information: <https://manned.org/ipcs>.

- Show information about all active IPC facilities:

`ipcs`

- Show information about active shared [m]emory segments, message [q]ueues or [s]empahore sets:

`ipcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--shmems|--queues|--semaphores</span>

- Show full details on the resource with a specific [i]D:

`ipcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--shmems|--queues|--semaphores</span>` --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_id</span>

- Show [l]imits in [b]ytes or in a human-readable format:

`ipcs --limits `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--bytes|--human</span>

- Show s[u]mmary about current usage:

`ipcs --summary`

- Show [c]reator's and owner's UIDs and PIDs for all IPC facilities:

`ipcs --creator`

- Show the [p]ID of the last operators for all IPC facilities:

`ipcs --pid`

- Show last access [t]imes for all IPC facilities:

`ipcs --time`
