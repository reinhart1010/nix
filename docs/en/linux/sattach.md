---
layout: page
title: linux/sattach (English)
description: "Attach to a Slurm job step."
content_hash: 3e671c2714159f00f204019bae65983e7b4af974
last_modified_at: 2023-12-19
tldri18n_status: 2
---
# sattach

Attach to a Slurm job step.
More information: <https://slurm.schedmd.com/sattach.html>.

- Redirect the IO streams (`stdout`, `stderr`, and `stdin`) of a Slurm job step to the current terminal:

`sattach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jobid</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stepid</span>

- Use the current console's input as `stdin` to the specified task:

`sattach --input-filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_number</span>

- Only redirect `stdin`/`stderr` of the specified task:

`sattach --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output|error</span>`-filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_number</span>
