---
layout: page
title: osx/log (English)
description: "View, export, and configure logging systems."
content_hash: 20197b4af08b009ddc316f911d1389b6b88aed19
---
# log

View, export, and configure logging systems.
More information: <https://www.dssw.co.uk/reference/log.html>.

- Stream live system logs:

`log stream`

- Stream logs sent to `syslog` from the process with a specific PID:

`log stream --process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>

- Show logs sent to syslog from a process with a specific name:

`log show --predicate "process == '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>`'"`

- Export all logs to disk for the past hour:

`sudo log collect --last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1h</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.logarchive</span>
