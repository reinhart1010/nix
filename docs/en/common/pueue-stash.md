---
layout: page
title: common/pueue-stash (English)
description: "Stash tasks to prevent them starting automatically."
content_hash: 38c1a7c99879c9ddb459baf1d082bb62f13092bd
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pueue stash

Stash tasks to prevent them starting automatically.
See also `pueue start` and `pueue enqueue`.
More information: <https://github.com/Nukesor/pueue>.

- Stash an enqueued task:

`pueue stash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Stash multiple tasks at once:

`pueue stash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Start a stashed task immediately:

`pueue start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Enqueue a task to be executed when preceding tasks finish:

`pueue enqueue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>
