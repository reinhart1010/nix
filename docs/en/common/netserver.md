---
layout: page
title: common/netserver (English)
description: "Server-side command for `netperf`, the benchmarking application that measures network throughput."
content_hash: 9c1867b5c7a7cd8a940ef173f70962b7251f6de4
last_modified_at: 2024-01-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/netserver.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># netserver

Server-side command for `netperf`, the benchmarking application that measures network throughput.
See also: `netperf`, for the client-side command.
More information: <https://manned.org/netserver.1>.

- Start a server on the default port (12865) and fork to background:

`netserver`

- Start server in foreground and do not fork:

`netserver -D`

- Specify [p]ort:

`netserver -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Force IPv[4] or IPv[6]:

`netserver -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>
