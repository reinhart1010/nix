---
layout: page
title: common/read (English)
description: "Shell builtin for retrieving data from `stdin`."
content_hash: 449db186876dbb4ad9b88d4d59aea265dcc01f9b
last_modified_at: 2024-08-05
tldri18n_status: 2
---
# read

Shell builtin for retrieving data from `stdin`.
More information: <https://manned.org/read.1p>.

- Store data that you type from the keyboard:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Store each of the next lines you enter as values of an array:

`read -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">array</span>

- Specify the number of maximum characters to be read:

`read -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">character_count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Assign multiple values to multiple variables:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "The name is Bond"</span>` | read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">_ variable1 _ variable2</span>

- Do not let backslash (\\) act as an escape character:

`read -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Display a prompt before the input:

`read -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Enter your input here: </span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Do not echo typed characters (silent mode):

`read -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Read `stdin` and perform an action on every line:

`while read line; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo|ls|rm|...</span>` "$line"; done < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/stdin|path/to/file|...</span>
