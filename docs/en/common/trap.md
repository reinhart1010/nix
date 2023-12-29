---
layout: page
title: common/trap (English)
description: "Automatically execute commands after receiving signals by processes or the operating system."
content_hash: c234dfefd8899dcf848248d266b95ce3f266a46a
last_modified_at: 2023-12-29
related_topics:
  - title: 中文 version
    url: /zh/common/trap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# trap

Automatically execute commands after receiving signals by processes or the operating system.
Can be used to perform cleanups for interruptions by the user or other actions.
More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#trap>.

- List active traps for the current shell:

`trap`

- Set a trap to execute commands when one or more signals are detected:

`trap 'echo "Caught signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>`"' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>

- Remove active traps:

`trap - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGHUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGINT</span>
