---
layout: page
title: openbsd/pkg_info (English)
description: "View information about packages in OpenBSD."
content_hash: c963a2846fde85d5ef8922e0de5bc4e2558b9c55
last_modified_at: 2023-10-22
---
# pkg_info

View information about packages in OpenBSD.
See also: `pkg_add`, `pkg_delete`.
More information: <https://man.openbsd.org/pkg_info>.

- Search for a package using the package name:

`pkg_info -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Output a list of installed packages for use with `pkg_add -l`:

`pkg_info -mz`
