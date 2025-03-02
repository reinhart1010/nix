---
layout: page
title: common/timeout (English)
description: "Run a command with a time limit."
content_hash: afb8b9b3b5d9d57c938240eec52f7be313014b9c
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/timeout.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/timeout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# timeout

Run a command with a time limit.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html>.

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
