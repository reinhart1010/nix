---
layout: page
title: linux/trace-cmd (English)
description: "Utility to interact with the Ftrace Linux kernel internal tracer."
content_hash: 2b076564995265a086ccae30c82ad24c51b50f6f
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># trace-cmd

Utility to interact with the Ftrace Linux kernel internal tracer.
This utility only runs as root.
More information: <https://manned.org/trace-cmd>.

- Display the status of tracing system:

`trace-cmd stat`

- List available tracers:

`trace-cmd list -t`

- Start tracing with a specific plugin:

`trace-cmd start -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timerlat|osnoise|hwlat|blk|mmiotrace|function_graph|wakeup_dl|wakeup_rt|wakeup|function|nop</span>

- View the trace output:

`trace-cmd show`

- Stop the tracing but retain the buffers:

`trace-cmd stop`

- Clear the trace buffers:

`trace-cmd clear`

- Clear the trace buffers and stop tracing:

`trace-cmd reset`
