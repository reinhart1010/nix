---
layout: page
title: linux/autorecon (English)
description: "A multi-threaded network reconnaissance tool which performs automated enumeration of services."
content_hash: 021bbce797728bb0b57e1017df8a23c38d19bee4
last_modified_at: 2024-04-10
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/autorecon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># autorecon

A multi-threaded network reconnaissance tool which performs automated enumeration of services.
More information: <https://github.com/Tib3rius/AutoRecon>.

- Perform reconnaissance on target host(s) (detailed scan results will be dumped in `./results`):

`sudo autorecon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_or_ip1,host_or_ip2,...</span>

- Perform reconnaissance on [t]arget(s) from a file:

`sudo autorecon --target-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- [o]utput results to a different directory:

`sudo autorecon --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/results</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_or_ip1,host_or_ip2,...</span>

- Limit scanning to specific [p]orts and protocols (`T` for TCP, `U` for UDP, `B` for both):

`sudo autorecon --ports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">T:21-25,80,443,U:53,B:123</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_or_ip1,host_or_ip2,...</span>
