---
layout: page
title: common/wait (English)
description: "Wait for a process to complete before proceeding."
content_hash: f57c8b21cc9baa4c0ea495b35bf2906f2d6db0f9
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# wait

Wait for a process to complete before proceeding.
More information: <https://manned.org/wait>.

- Wait for a process to finish given its process ID (PID) and return its exit status:

`wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Wait for all processes known to the invoking shell to finish:

`wait`

- Wait for a job to finish:

`wait %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>
