---
layout: page
title: linux/lsipc (English)
description: "Show information on System V IPC facilities currently employed in the system."
content_hash: c1840833960f8eaa7769017a9934ccb7e2f69cc7
last_modified_at: 2024-05-08
tldri18n_status: 2
---
# lsipc

Show information on System V IPC facilities currently employed in the system.
See also: `ipcs` for the older tool.
More information: <https://manned.org/lsipc>.

- Show information about all active IPC facilities:

`lsipc`

- Show information about active shared [m]emory segments, message [q]ueues or [s]empahore sets:

`lsipc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--shmems|--queues|--semaphores</span>

- Show full details on the resource with a specific [i]D:

`lsipc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--shmems|--queues|--semaphores</span>` --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_id</span>

- Print the given [o]utput columns (see all supported columns with `--help`):

`lsipc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">KEY,ID,PERMS,SEND,STATUS,NSEMS,RESOURCE,...</span>

- Use [r]aw, [J]SON, [l]ist or [e]xport (key="value") format:

`lsipc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--raw|--json|--list|--export</span>

- Don't truncate the output:

`lsipc --notruncate`
