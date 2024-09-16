---
layout: page
title: common/tspin (English)
description: "A log file highlighter based on the `less` pager and basically behaves like any pager."
content_hash: a5b6ccb57f0a532b3cdf0359a6963d79238281fb
last_modified_at: 2024-09-16
tldri18n_status: 2
---
# tspin

A log file highlighter based on the `less` pager and basically behaves like any pager.
More information: <https://github.com/bensadeh/tailspin>.

- Read from file and view in `less`:

`tspin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/application.log</span>

- Read from another command and print to stdout:

`journalctl -b --follow | tspin`

- Read from file and print to `stdout`:

`tspin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/application.log</span>` --print`

- Read from stdin and print to `stdout`:

`echo "2021-01-01 12:00:00 [INFO] This is a log message" | tspin`
