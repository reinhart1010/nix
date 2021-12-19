---
layout: page
title: linux/sstat (English)
description: "View information about running jobs."
content_hash: d3159e69601b4863a899bdef231f6a2b5d28122b
---
# sstat

View information about running jobs.
More information: <https://slurm.schedmd.com/sstat.html>.

- Display status information of a comma-separated list of jobs:

`sstat --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Display job ID, average CPU and average virtual memory size of a comma-separated list of jobs, with pipes as column delimiters:

`sstat --parsable --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JobID</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AveCPU</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AveVMSize</span>

- Display list of fields available:

`sstat --helpformat`
