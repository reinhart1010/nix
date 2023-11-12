---
layout: page
title: common/pueue-follow (English)
description: "Follow the output of a currently running task."
content_hash: f859cc4c9ea5d2a58a1d56e19914145e14f8a9d4
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pueue follow

Follow the output of a currently running task.
See also: `pueue log`.
More information: <https://github.com/Nukesor/pueue>.

- Follow the output of a task (`stdout` + `stderr`):

`pueue follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Follow `stderr` of a task:

`pueue follow --err `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>
