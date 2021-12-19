---
layout: page
title: linux/sbatch (English)
description: "Submit a batch job to the SLURM scheduler."
content_hash: 9a0b58d38d3ae18712ce1d5612f8a841e7486d52
---
# sbatch

Submit a batch job to the SLURM scheduler.

- Submit a batch job:

`sbatch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/job.sh</span>

- Submit a batch job with a custom name:

`sbatch --job-name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myjob</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/job.sh</span>

- Submit a batch job with a time limit of 30 minutes:

`sbatch --time=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">00:30:00</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/job.sh</span>

- Submit a job and request multiple nodes:

`sbatch --nodes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/job.sh</span>
