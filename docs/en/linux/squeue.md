---
layout: page
title: linux/squeue (English)
description: "View the jobs queued in the SLURM scheduler."
content_hash: 1f4f206f4ebad2fe5d1fcefc9fd37fc8290d5403
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# squeue

View the jobs queued in the SLURM scheduler.
More information: <https://manned.org/squeue>.

- View the queue:

`squeue`

- View jobs queued by a specific user:

`squeue -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- View the queue and refresh every 5 seconds:

`squeue -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- View the queue with expected start times:

`squeue --start`
