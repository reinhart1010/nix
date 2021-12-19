---
layout: page
title: linux/taskset (English)
description: "Get or set a process' CPU affinity or start a new process with a defined CPU affinity."
content_hash: 082d52190b2c57529a2108109dc1275ea7f55506
---
# taskset

Get or set a process' CPU affinity or start a new process with a defined CPU affinity.

- Get a running process' CPU affinity by PID:

`taskset --pid --cpu-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Set a running process' CPU affinity by PID:

`taskset --pid --cpu-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Start a new process with affinity for a single CPU:

`taskset --cpu-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Start a new process with affinity for multiple non-sequential CPUs:

`taskset --cpu-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id_2</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id_3</span>

- Start a new process with affinity for CPUs 1 through 4:

`taskset --cpu-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id_1</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_id_4</span>
