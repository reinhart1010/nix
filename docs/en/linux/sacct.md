---
layout: page
title: linux/sacct (English)
description: "Display accounting data from the Slurm service."
content_hash: fcfc9cf29ac06db2b74d91f267abf2b8be7d55a3
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# sacct

Display accounting data from the Slurm service.
More information: <https://slurm.schedmd.com/sacct.html>.

- Display job ID, job name, partition, account, number of allocated cpus, job state, and job exit codes for recent jobs:

`sacct`

- Display job ID, job state, job exit code for recent jobs:

`sacct --brief`

- Display the allocations of a job:

`sacct --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` --allocations`

- Display elapsed time, job name, number of requested CPUs, and memory requested of a job:

`sacct --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` --format=Elapsed,JobName,ReqCPUS,ReqMem`

- Display recent jobs that occurred from one week ago up to the present day:

`sacct --starttime=$(date -d "1 week ago" +'%F')`

- Output a larger number of characters for an attribute:

`sacct --format=JobID,JobName%100`
