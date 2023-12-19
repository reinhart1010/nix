---
layout: page
title: linux/sprio (English)
description: "View the factors determining a job's scheduling priority."
content_hash: 6d13f7c4581c284a0880e8efc57a7bbf07a9f7ca
last_modified_at: 2023-12-19
tldri18n_status: 2
---
# sprio

View the factors determining a job's scheduling priority.
More information: <https://slurm.schedmd.com/sprio.html>.

- View the factors determining the scheduling priority of all jobs:

`sprio`

- View the factors determining the specified job's scheduling priority:

`sprio --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id_1,job_id_2,...</span>

- Output additional information:

`sprio --long`

- View information for the jobs of specified users:

`sprio --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_name_1,user_name_2,...</span>

- Print the weights for each factor determining job scheduling priority:

`sprio --weights`
