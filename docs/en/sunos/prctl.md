---
layout: page
title: sunos/prctl (English)
description: "Get or set the resource controls of running processes,."
content_hash: bfeb6c2e2a6291e771f88094aac96a7d278b548f
---
# prctl

Get or set the resource controls of running processes,.
Tasks, and projects.
More information: <https://www.unix.com/man-page/sunos/1/prctl>.

- Examine process limits and permissions:

`prctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Examine process limits and permissions in machine parsable format:

`prctl -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Get specific limit for a running process:

`prctl -n process.max-file-descriptor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>
