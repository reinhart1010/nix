---
layout: page
title: linux/pw-top (English)
description: "View the PipeWire nodes and devices statistics in real-time."
content_hash: 1d23737d1d589f02087508c833bb09895d8f54fd
last_modified_at: 2024-01-03
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-top.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-top

View the PipeWire nodes and devices statistics in real-time.
See also: `pipewire`, `pw-dump`, `pw-cli`, `pw-profiler`.
More information: <https://docs.pipewire.org/page_man_pw-top_1.html>.

- Display an interactive view of PipeWire nodes and devices:

`pw-top`

- Monitor a remote instance:

`pw-top --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Print information periodically instead of running in interactive mode:

`pw-top --batch-mode`

- Print information periodically for a specific number of times:

`pw-top --batch-mode --iterations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
