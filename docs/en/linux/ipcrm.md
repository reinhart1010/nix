---
layout: page
title: linux/ipcrm (English)
description: "Delete IPC (Inter-process Communication) resources."
content_hash: 3c0551073eea73b898462a5fcebcb570b2ad39f7
---
# ipcrm

Delete IPC (Inter-process Communication) resources.
More information: <https://manned.org/ipcrm>.

- Delete a shared memory segment by ID:

`ipcrm --shmem-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shmem_id</span>

- Delete a shared memory segment by key:

`ipcrm --shmem-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shmem_key</span>

- Delete an IPC queue by ID:

`ipcrm --queue-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ipc_queue_id</span>

- Delete an IPC queue by key:

`ipcrm --queue-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ipc_queue_key</span>

- Delete a semaphore by ID:

`ipcrm --semaphore-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">semaphore_id</span>

- Delete a semaphore by key:

`ipcrm --semaphore-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">semaphore_key</span>

- Delete all IPC resources:

`ipcrm --all`
