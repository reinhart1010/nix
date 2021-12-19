---
layout: page
title: common/pueue-parallel (English)
description: "Set the amount of allowed parallel tasks."
content_hash: 3c1e05de5220e7cc9d7db02f11e144d42e3491e3
---
# pueue parallel

Set the amount of allowed parallel tasks.
More information: <https://github.com/Nukesor/pueue>.

- Set the maximum number of tasks allowed to run in parallel, in the default group:

`pueue parallel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">max_number_of_parallel_tasks</span>

- Set the maximum number of tasks allowed to run in parallel, in a specific group:

`pueue parallel --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maximum_number_of_parallel_tasks</span>
