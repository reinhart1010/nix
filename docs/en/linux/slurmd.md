---
layout: page
title: linux/slurmd (English)
description: "Monitors all tasks running on the compute node, accepts tasks, launches tasks, and kills running tasks upon request."
content_hash: fbaf4511f735e953477b55f01f01c0354d17e142
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# slurmd

Monitors all tasks running on the compute node, accepts tasks, launches tasks, and kills running tasks upon request.
More information: <https://slurm.schedmd.com/slurmd.html>.

- Report node rebooted when daemon restarted (Used for testing purposes):

`slurmd -b`

- Run the daemon with the given nodename:

`slurmd -N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodename</span>

- Write log messages to the specified file:

`slurmd -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Read configuration from the specified file:

`slurmd -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display help:

`slurmd -h`
