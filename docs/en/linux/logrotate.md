---
layout: page
title: linux/logrotate (English)
description: "Rotates, compresses, and mails system logs."
content_hash: 0ea4c48ebd2cc7298cfb9cb1abc688bf7a3a22a3
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># logrotate

Rotates, compresses, and mails system logs.
More information: <https://manned.org/logrotate>.

- Trigger a run manually:

`logrotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/logrotate.conf</span>` --force`

- Run using a specific command to mail reports:

`logrotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/logrotate.conf</span>` --mail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/bin/mail_command</span>

- Run without using a state (lock) file:

`logrotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/logrotate.conf</span>` --state /dev/null`

- Run and skip the state (lock) file check:

`logrotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/logrotate.conf</span>` --skip-state-lock`

- Tell `logrotate` to log verbose output into the log file:

`logrotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/logrotate.conf</span>` --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/log_file</span>
