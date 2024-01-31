---
layout: page
title: linux/sstat (English)
description: "View information about running jobs."
content_hash: c8e64c15ae8173abe962499819bdd4e09966a563
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# sstat

View information about running jobs.
More information: <https://slurm.schedmd.com/sstat.html>.

- Display status information of a comma-separated list of jobs:

`sstat --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Display job ID, average CPU and average virtual memory size of a comma-separated list of jobs, with pipes as column delimiters:

`sstat --parsable --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JobID,AveCPU,AveVMSize</span>

- Display list of fields available:

`sstat --helpformat`
