---
layout: page
title: common/nbtscan (English)
description: "Scan networks for NetBIOS name information."
content_hash: 47e0f4837b356f0bff60a2f46dd1dcbb9e3bf637
---
# nbtscan

Scan networks for NetBIOS name information.
More information: <https://github.com/resurrecting-open-source-projects/nbtscan>.

- Scan a network for NetBIOS names:

`nbtscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1/24</span>

- Scan a single IP address:

`nbtscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>

- Display verbose output:

`nbtscan -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1/24</span>

- Display output in `/etc/hosts` format:

`nbtscan -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1/24</span>

- Read IP addresses / networks to scan from a file:

`nbtscan -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>
