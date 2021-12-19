---
layout: page
title: common/timeout (English)
description: "Run a command with a time limit."
content_hash: 25cc2f8bceb6d228074f97c6df7ecc7afef65252
---
# timeout

Run a command with a time limit.
More information: <https://www.gnu.org/software/coreutils/timeout>.

- Run `sleep 10` and terminate it, if it runs for more than 3 seconds:

`timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sleep 10</span>

- Specify the signal to be sent to the command after the time limit expires. (By default, TERM is sent):

`timeout --signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sleep 10</span>
