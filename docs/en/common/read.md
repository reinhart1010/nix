---
layout: page
title: common/read (English)
description: "Shell builtin for retrieving data from `stdin`."
content_hash: c69af816601dfeac20a55623c4fe6544a9dfcd20
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# read

Shell builtin for retrieving data from `stdin`.
More information: <https://manned.org/read.1p>.

- Store data that you type from the keyboard:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Do not let backslash (\\) act as an escape character:

`read -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Read `stdin` and perform an action on every line:

`while read line; do echo "$line"; done`
