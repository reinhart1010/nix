---
layout: page
title: common/logger (English)
description: "Add messages to syslog (/var/log/syslog)."
content_hash: c561215f12f84820e11a4a382d46b986497bcf86
related_topics:
  - title: 中文 version
    url: /zh/common/logger.html
    icon: bi bi-globe
---
# logger

Add messages to syslog (/var/log/syslog).
More information: <https://manned.org/logger>.

- Log a message to syslog:

`logger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>

- Take input from stdin and log to syslog:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">log_entry</span>` | logger`

- Send the output to a remote syslog server running at a given port. Default port is 514:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">log_entry</span>` | logger --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Use a specific tag for every line logged. Default is the name of logged in user:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">log_entry</span>` | logger --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Log messages with a given priority. Default is `user.notice`. See `man logger` for all priority options:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">log_entry</span>` | logger --priority `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user.warning</span>
