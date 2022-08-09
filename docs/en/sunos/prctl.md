---
layout: page
title: sunos/prctl (English)
description: "Get or set the resource controls of running processes, tasks, and projects."
content_hash: f8d8827cf7e840d6a54c7dfa338303d77c262e3b
---
# prctl

Get or set the resource controls of running processes, tasks, and projects.
More information: <https://www.unix.com/man-page/sunos/1/prctl>.

- Examine process limits and permissions:

`prctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Examine process limits and permissions in machine parsable format:

`prctl -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Get specific limit for a running process:

`prctl -n process.max-file-descriptor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>
