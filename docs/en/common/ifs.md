---
layout: page
title: common/ifs (English)
description: "IFS (Internal Field Separator) is a special environment variable that defines the delimiter used for word splitting in Unix shells."
content_hash: 56e8b058a68a96d9c917a39d00451b9658c4d358
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# IFS

IFS (Internal Field Separator) is a special environment variable that defines the delimiter used for word splitting in Unix shells.
The default value of IFS is a space, tab, and newline. The three characters serve as delimiters.
More information: <https://www.gnu.org/software/bash/manual/html_node/Word-Splitting.html>.

- View the current IFS value:

`echo "$IFS"`

- Change the IFS value:

`IFS="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>`"`

- Reset IFS to default:

`IFS=$' \t\n'`

- Temporarily change the IFS value in a subshell:

`(IFS="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>`"; echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">one:two:three</span>`")`
