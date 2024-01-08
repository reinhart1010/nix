---
layout: page
title: linux/trap (English)
description: "Execute a command upon an event."
content_hash: f6dda0af6f6460d0cd326f03ecbf86de14b7fde2
last_modified_at: 2024-01-08
tldri18n_status: 2
---
# trap

Execute a command upon an event.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-trap>.

- List the available event names (e.g. `SIGWINCH`):

`trap -l`

- List the commands and the names of the expected events:

`trap -p`

- Execute a command when a signal is received:

`trap 'echo "Caught signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>`"' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>

- Remove commands:

`trap - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGINT</span>
