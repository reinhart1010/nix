---
layout: page
title: linux/sacct (English)
description: "Display accounting data from the Slurm service."
content_hash: c5590ebfdf00136d3726b6afeb7b58eaf61c66df
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# sacct

Display accounting data from the Slurm service.
More information: <https://slurm.schedmd.com/sacct.html>.

- Display job id, job name, partition, account, number of allocated cpus, job state, and job exit codes for recent jobs:

`sacct`

- Display job id, job state, job exit code for recent jobs:

`sacct --brief`

- Display the allocations of a job:

`sacct --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` --allocations`

- Display elapsed time, job name, number of requested CPUs, and memory requested of a job:

`sacct --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">elapsed</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jobname</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reqcpus</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reqmem</span>
