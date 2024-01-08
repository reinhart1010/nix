---
layout: page
title: common/trap (English)
description: "Execute a command upon an event."
content_hash: 99f75697e01f125a7cb3a5023fdad6c2ae9647b0
last_modified_at: 2024-01-08
related_topics:
  - title: 中文 version
    url: /zh/common/trap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# trap

Execute a command upon an event.
More information: <https://manned.org/trap.1posix>.

- List the commands and the names of the expected events:

`trap`

- Execute a command when a signal is received:

`trap 'echo "Caught signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>`"' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HUP</span>

- Remove commands:

`trap - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INT</span>
