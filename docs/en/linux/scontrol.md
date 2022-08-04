---
layout: page
title: linux/scontrol (English)
description: "View information about and modify jobs."
content_hash: d4f5d49ef6f562b62180132adf492ffc6c440b2e
---
# scontrol

View information about and modify jobs.
More information: <https://slurm.schedmd.com/scontrol.html>.

- Show information for job:

`scontrol show job `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Suspend a comma-separated list of running jobs:

`scontrol suspend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Resume a comma-separated list of suspended jobs:

`scontrol resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Hold a comma-separated list of queued jobs (Use `release` command to permit the jobs to be scheduled):

`scontrol hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Release a comma-separated list of suspended job:

`scontrol release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>
