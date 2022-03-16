---
layout: page
title: linux/mktemp (English)
description: "Create a temporary file or directory."
content_hash: e5a2bdd3e72761893cd757967814386bf782ca60
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mktemp

Create a temporary file or directory.
More information: <https://www.gnu.org/software/autogen/mktemp.html>.

- Create an empty temporary file and print the absolute path to it:

`mktemp`

- Create an empty temporary file with a given suffix and print the absolute path to file:

`mktemp --suffix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ext</span>`"`

- Create a temporary directory and print the absolute path to it:

`mktemp --directory`
