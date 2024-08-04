---
layout: page
title: common/read (English)
description: "Shell builtin for retrieving data from `stdin`."
content_hash: 213c591852c75d2de0ac217e70bf5266b977a4e6
last_modified_at: 2024-08-04
tldri18n_status: 2
---
# read

Shell builtin for retrieving data from `stdin`.
More information: <https://manned.org/read.1p>.

- Store data that you type from the keyboard:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Do not let backslash (\\) act as an escape character:

`read -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Read `stdin` or file and perform an action on every line:

`while read line; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo|ls|rm|...</span>` "$line"; done < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/stdin|path/to/file|...</span>
