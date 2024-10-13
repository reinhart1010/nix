---
layout: page
title: linux/journalctl (English)
description: "Query the systemd journal."
content_hash: 5a45cc09f1810e37beac68d12025873b9ca7ed3d
last_modified_at: 2024-10-13
related_topics:
  - title: español version
    url: /es/linux/journalctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/journalctl.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/journalctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# journalctl

Query the systemd journal.
More information: <https://manned.org/journalctl>.

- Show all messages with priority level 3 (errors) from this [b]oot:

`journalctl -b --priority=3`

- Delete journal logs which are older than 2 days:

`journalctl --vacuum-time=2d`

- Show only the last N li[n]es and [f]ollow new messages (like `tail -f` for traditional syslog):

`journalctl --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` --follow`

- Show all messages by a specific [u]nit:

`journalctl --unit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit</span>

- Show logs for a given unit since the last time it started:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit</span>`)`

- Filter messages within a time range (either timestamp or placeholders like "yesterday"):

`journalctl --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">now|today|yesterday|tomorrow</span>` --until "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD HH:MM:SS</span>`"`

- Show all messages by a specific process:

`journalctl _PID=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Show all messages by a specific executable:

`journalctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>
