---
layout: page
title: common/netperf (English)
description: "Client-side command for `netperf`, the benchmarking application that measures network throughput. Similar to `iperf`."
content_hash: 1db4f57813c5005ed6fc620486fdb8b8ddc99a54
last_modified_at: 2024-01-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/netperf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># netperf

Client-side command for `netperf`, the benchmarking application that measures network throughput. Similar to `iperf`.
See also: `netserver`, for the server-side command.
More information: <https://hewlettpackard.github.io/netperf/doc/netperf.html#Global-Command_002dline-Options>.

- Connect to server on a specific IP address via default port (12865):

`netperf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- Specify [p]ort:

`netperf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Specify the sampling [l]ength in seconds (default is 10):

`netperf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>

- Force IPv[4] or IPv[6]:

`netperf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>
