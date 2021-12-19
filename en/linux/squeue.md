---
layout: page
title: linux/squeue (English)
description: "View the jobs queued in the SLURM scheduler."
content_hash: 6e64963e660cd85513e85fb108d9ef0e73b39b62
---
# squeue

View the jobs queued in the SLURM scheduler.

- View the queue:

`squeue`

- View jobs queued by a specific user:

`squeue -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- View the queue and refresh every 5 seconds:

`squeue -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- View the queue with expected start times:

`squeue --start`
