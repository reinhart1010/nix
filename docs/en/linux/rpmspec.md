---
layout: page
title: linux/rpmspec (English)
description: "Query a RPM spec file."
content_hash: 28a18be028be6f8ca69bd5d894ac0f47212c2bf1
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rpmspec

Query a RPM spec file.
More information: <https://manned.org/rpmspec>.

- List binary packages which would be generated from a rpm spec file:

`rpmspec --query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/rpm.spec</span>

- List all options for `--queryformat`:

`rpmspec --querytags`

- Get summary information for single binary packages generated from a rpm spec file:

`rpmspec --query --queryformat "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%{name}: %{summary}\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/rpm.spec</span>

- Get the source package which would be generated from a rpm spec file:

`rpmspec --query --srpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/rpm.spec</span>

- Parse a rpm spec file to `stdout`:

`rpmspec --parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/rpm.spec</span>
