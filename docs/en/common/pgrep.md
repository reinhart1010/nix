---
layout: page
title: common/pgrep (English)
description: "Find or signal processes by name."
content_hash: b48c9235af58186dde690b33e38ff686765c17f5
last_modified_at: 2024-06-18
tldri18n_status: 2
---
# pgrep

Find or signal processes by name.
More information: <https://www.manned.org/pgrep>.

- Return PIDs of any running processes with a matching command string:

`pgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- Search for processes including their command-line options:

`pgrep --full "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parameter</span>`"`

- Search for processes run by a specific user:

`pgrep --euid root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>
