---
layout: page
title: common/mktemp (English)
description: "Create a temporary file or directory."
content_hash: dbb2f7cf52a6dfa365df10f570f4565601311077
---
# mktemp

Create a temporary file or directory.
More information: <https://www.gnu.org/software/autogen/mktemp.html>.

- Create an empty temporary file and print the absolute path to it:

`mktemp`

- Create an empty temporary file with a given suffix and print the absolute path to file:

`mktemp --suffix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ext</span>`"`

- Create a temporary directory and print the absolute path to it (non-portable long option: --directory):

`mktemp -d`
