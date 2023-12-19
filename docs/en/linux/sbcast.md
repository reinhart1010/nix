---
layout: page
title: linux/sbcast (English)
description: "Send a file to a job's allocated nodes."
content_hash: e7188284e8754040bb7dba8bde36e5e25a106d73
last_modified_at: 2023-12-19
tldri18n_status: 2
---
# sbcast

Send a file to a job's allocated nodes.
This command should only be used from within a Slurm batch job.
More information: <https://slurm.schedmd.com/sbcast.html>.

- Send a file to all nodes allocated to the current job:

`sbcast `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>

- Autodetect shared libraries the transmitted file depends upon and transmit them as well:

`sbcast --send-libs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>
