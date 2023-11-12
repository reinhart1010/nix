---
layout: page
title: linux/systemd-cat (English)
description: "Connect a pipeline or program's output streams with the systemd journal."
content_hash: fc8af8a1868161042e56ced2dde324d597e7afea
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# systemd-cat

Connect a pipeline or program's output streams with the systemd journal.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-cat.html>.

- Write the output of the specified command to the journal (both output streams are captured):

`systemd-cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Write the output of a pipeline to the journal (`stderr` stays connected to the terminal):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | systemd-cat`
