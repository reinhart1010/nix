---
layout: page
title: common/timeout (English)
description: "Run a command with a time limit."
content_hash: 0a116b02fa5008a6ea0525fde786089f368f23ca
last_modified_at: 2024-02-09
tldri18n_status: 2
---
# timeout

Run a command with a time limit.
More information: <https://www.gnu.org/software/coreutils/timeout>.

- Run `sleep 10` and terminate it after 3 seconds:

`timeout 3s sleep 10`

- Send a signal to the command after the time limit expires (SIGTERM by default):

`timeout --signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sleep 10</span>
