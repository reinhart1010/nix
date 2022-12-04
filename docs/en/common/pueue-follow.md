---
layout: page
title: common/pueue-follow (English)
description: "Follow the output of a currently running task."
content_hash: f9576fb105d362d9c40767c3a32984118e03624c
last_modified_at: 2022-12-04
---
# pueue follow

Follow the output of a currently running task.
See also: `pueue log`.
More information: <https://github.com/Nukesor/pueue>.

- Follow the output of a task (`stdout` + `stderr`):

`pueue follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Follow the `stderr` of a task:

`pueue follow --err `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>
