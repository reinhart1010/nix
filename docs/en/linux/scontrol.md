---
layout: page
title: linux/scontrol (English)
description: "View information about and modify jobs."
content_hash: 3fb76027141f9e210add0b978693d4046a970e80
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# scontrol

View information about and modify jobs.
More information: <https://slurm.schedmd.com/scontrol.html>.

- Show information for job:

`scontrol show job `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Suspend a comma-separated list of running jobs:

`scontrol suspend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id1,job_id2,...</span>

- Resume a comma-separated list of suspended jobs:

`scontrol resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id1,job_id2,...</span>

- Hold a comma-separated list of queued jobs (Use `release` command to permit the jobs to be scheduled):

`scontrol hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id1,job_id2,...</span>

- Release a comma-separated list of suspended job:

`scontrol release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id1,job_id2,...</span>
