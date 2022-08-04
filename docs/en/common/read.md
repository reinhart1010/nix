---
layout: page
title: common/read (English)
description: "BASH builtin for retrieving data from standard input."
content_hash: 9f07ae9dfdef2ebfdfed6a1fccd2adc00e465aef
---
# read

BASH builtin for retrieving data from standard input.
More information: <https://manned.org/read.1p>.

- Store data that you type from the keyboard:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Store each of the next lines you enter as values of an array:

`read -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">array</span>

- Specify the number of maximum characters to be read:

`read -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">character_count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Use a specific character as a delimiter instead of a new line:

`read -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_delimiter</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Do not let backslash (\) act as an escape character:

`read -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Display a prompt before the input:

`read -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Enter your input here: </span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Do not echo typed characters (silent mode):

`read -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Read stdin and perform an action on every line:

`while read line; do echo "$line"; done`
