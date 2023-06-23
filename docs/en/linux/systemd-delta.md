---
layout: page
title: linux/systemd-delta (English)
description: "Find overridden systemd-related configuration files."
content_hash: 5bdff561bbf8df1164e9d8d582af262be71259fc
last_modified_at: 2023-06-23
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># systemd-delta

Find overridden systemd-related configuration files.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-delta.html>.

- Show all overridden configuration files:

`systemd-delta`

- Show only files of specific types (comma-separated list):

`systemd-delta --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">masked|equivalent|redirected|overridden|extended|unchanged</span>

- Show only files whose path starts with the specified prefix (Note: a prefix is a directory containing subdirectories with systemd configuration files):

`systemd-delta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc|/run|/usr/lib|...</span>

- Further restrict the search path by adding a suffix (the prefix is optional):

`systemd-delta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfiles.d|sysctl.d|systemd/system|...</span>
