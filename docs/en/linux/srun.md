---
layout: page
title: linux/srun (English)
description: "Create an interactive slurm job or connect to an existing job."
content_hash: d57e5ed57051bc70e25146194a2971f84c1fbb88
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# srun

Create an interactive slurm job or connect to an existing job.
More information: <https://slurm.schedmd.com/srun.html>.

- Submit a basic interactive job:

`srun --pty /bin/bash`

- Submit an interactive job with different attributes:

`srun --ntasks-per-node=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num_cores</span>` --mem-per-cpu=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">memory_MB</span>` --pty /bin/bash`

- Connect to a worker node with a job running:

`srun --jobid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` --pty /bin/bash`
