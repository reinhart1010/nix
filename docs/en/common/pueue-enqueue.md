---
layout: page
title: common/pueue-enqueue (English)
description: "Enqueue stashed tasks."
content_hash: 55da00a38b35430573835ef2ef795131c1ddf1bd
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pueue enqueue

Enqueue stashed tasks.
See also: `pueue stash`.
More information: <https://github.com/Nukesor/pueue>.

- Enqueue multiple stashed tasks at once:

`pueue enqueue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Enqueue a stashed task after 60 seconds:

`pueue enqueue --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Enqueue a stashed task next Wednesday:

`pueue enqueue --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wednesday</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Enqueue a stashed task after four months:

`pueue enqueue --delay "4 months" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Enqueue a stashed task on 2021-02-19:

`pueue enqueue --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2021-02-19</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- List all available date/time formats:

`pueue enqueue --help`
