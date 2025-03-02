---
layout: page
title: linux/trap (English)
description: "Execute a command upon an event."
content_hash: 37cafdf13cf924d8a7f49120d515a6b8531a4941
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/trap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# trap

Execute a command upon an event.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-trap>.

- List the available event names (e.g. `SIGWINCH`):

`trap -l`

- List the commands and the names of the expected events:

`trap`

- Execute a command when a signal is received:

`trap 'echo "Caught signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>`"' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>

- Remove commands:

`trap - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGINT</span>

- Ignore a signal:

`trap '' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGINT</span>
