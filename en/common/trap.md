---
layout: page
title: common/trap (English)
description: "Automatically execute commands after receiving signals by processes or the operating system."
content_hash: d499954498b0bbcc39e122d9f46f391b077fe1f0
related_topics:
  - title: 中文 version
    url: /zh/common/trap.html
    icon: bi bi-globe
---
# trap

Automatically execute commands after receiving signals by processes or the operating system.
Can be used to perform cleanups for interruptions by the user or other actions.
More information: <https://manned.org/trap>.

- List available signals to set traps for:

`trap -l`

- List active traps for the current shell:

`trap -p`

- Set a trap to execute commands when one or more signals are detected:

`trap 'echo "Caught signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>`"' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>

- Remove active traps:

`trap - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGINT</span>
