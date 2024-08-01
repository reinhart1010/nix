---
layout: page
title: common/timeout (English)
description: "Run a command with a time limit."
content_hash: 66aba87ee709cbbff0be9d8f45f2d0f5fafd0753
last_modified_at: 2024-08-01
related_topics:
  - title: Nederlands version
    url: /nl/common/timeout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# timeout

Run a command with a time limit.
More information: <https://www.gnu.org/software/coreutils/timeout>.

- Run `sleep 10` and terminate it after 3 seconds:

`timeout 3s sleep 10`

- Send a [s]ignal to the command after the time limit expires (`TERM` by default, `kill -l` to list all signals):

`timeout --signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INT|HUP|KILL|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sleep 10</span>

- Send [v]erbose output to `stderr` showing signal sent upon timeout:

`timeout --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5s|1m|1h|1d|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Preserve the exit status of the command regardless of timing out:

`timeout --preserve-status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1s|1m|1h|1d|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Send a forceful `KILL` signal after certain duration if the command ignores initial signal upon timeout:

`timeout --kill-after=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
