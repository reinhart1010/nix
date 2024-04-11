---
layout: page
title: linux/autorecon (English)
description: "A multi-threaded network reconnaissance tool which performs automated enumeration of services."
content_hash: 021bbce797728bb0b57e1017df8a23c38d19bee4
last_modified_at: 2024-04-11
tldri18n_status: 2
---
# autorecon

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
