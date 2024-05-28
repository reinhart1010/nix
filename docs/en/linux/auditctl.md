---
layout: page
title: linux/auditctl (English)
description: "Utility to control the behavior, get status and manage rules of the Linux Auditing System."
content_hash: f275e039b5d906502c8b673135c4152fb72d3233
last_modified_at: 2024-05-28
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/auditctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># auditctl

Utility to control the behavior, get status and manage rules of the Linux Auditing System.
More information: <https://manned.org/auditctl>.

- Display the [s]tatus of the audit system:

`sudo auditctl -s`

- [l]ist all currently loaded audit rules:

`sudo auditctl -l`

- [D]elete all audit rules:

`sudo auditctl -D`

- [e]nable/disable the audit system:

`sudo auditctl -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|0</span>

- Watch a file for changes:

`sudo auditctl -a always,exit -F arch=b64 -F path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>` -F perm=wa`

- Recursively watch a directory for changes:

`sudo auditctl -a always,exit -F arch=b64 -F dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/directory/</span>` -F perm=wa`

- Display [h]elp:

`auditctl -h`
