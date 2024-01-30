---
layout: page
title: linux/rpmspec (English)
description: "Query a RPM spec file."
content_hash: 364845315fcec8c5ee4ad4187feb516d74ee9b7d
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# rpmspec

Query a RPM spec file.
More information: <https://manned.org/rpmspec>.

- List binary packages which would be generated from a RPM spec file:

`rpmspec --query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/rpm.spec</span>

- List all options for `--queryformat`:

`rpmspec --querytags`

- Get summary information for single binary packages generated from a RPM spec file:

`rpmspec --query --queryformat "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%{name}: %{summary}\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/rpm.spec</span>

- Get the source package which would be generated from a RPM spec file:

`rpmspec --query --srpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/rpm.spec</span>

- Parse a RPM spec file to `stdout`:

`rpmspec --parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/rpm.spec</span>
