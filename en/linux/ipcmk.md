---
layout: page
title: linux/ipcmk (English)
description: "Create IPC (Inter-process Communication) resources."
content_hash: 6050f701492ddaccdd60c2a108f125d6bf9fcd66
---
# ipcmk

Create IPC (Inter-process Communication) resources.
More information: <https://manned.org/ipcmk>.

- Create a shared memory segment:

`ipcmk --shmem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segment_size_in_bytes</span>

- Create a semaphore:

`ipcmk --semaphore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">element_size</span>

- Create a message queue:

`ipcmk --queue`

- Create a shared memory segment with specific permissions (default is 0644):

`ipcmk --shmem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segment_size_in_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">octal_permissions</span>
