---
layout: page
title: common/gops (English)
description: "CLI tool which lists and diagnoses Go processes currently running on your system."
content_hash: cd0e56eb800eada9cb06d0877af3e54f6df3436d
---
# gops

CLI tool which lists and diagnoses Go processes currently running on your system.
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
