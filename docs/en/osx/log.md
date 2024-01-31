---
layout: page
title: osx/log (English)
description: "View, export, and configure logging systems."
content_hash: 8a1b86792a3f2f0b3573f788102170b998847278
last_modified_at: 2024-01-31
related_topics:
  - title: italiano version
    url: /it/osx/log.html
    icon: bi bi-globe
tldri18n_status: 2
---
# log

View, export, and configure logging systems.
More information: <https://keith.github.io/xcode-man-pages/log.1.html>.

- Stream live system logs:

`log stream`

- Stream logs sent to `syslog` from the process with a specific PID:

`log stream --process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>

- Show logs sent to syslog from a process with a specific name:

`log show --predicate "process == '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>`'"`

- Export all logs to disk for the past hour:

`sudo log collect --last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1h</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.logarchive</span>
