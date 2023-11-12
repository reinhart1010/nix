---
layout: page
title: common/gops (English)
description: "List and diagnose Go processes currently running on your system."
content_hash: f998fd1bebed1a16a629e8c8e4fe6ea89f78e5b0
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gops

List and diagnose Go processes currently running on your system.
More information: <https://github.com/google/gops>.

- Print all go processes running locally:

`gops`

- Print more information about a process:

`gops `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Display a process tree:

`gops tree`

- Print the current stack trace from a target program:

`gops stack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid|addr</span>

- Print the current runtime memory statistics:

`gops memstats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid|addr</span>
