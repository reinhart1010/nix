---
layout: page
title: linux/mktemp (English)
description: "Create a temporary file or directory."
content_hash: 70c1d1b7ff9865d79fc970e63807d380ef8cdb66
last_modified_at: 2023-08-31
---
# mktemp

Create a temporary file or directory.
Note that examples here all assume `$TMPDIR` is unset.
More information: <https://www.gnu.org/software/autogen/mktemp.html>.

- Create an empty temporary file in `/tmp/` and print its absolute path:

`mktemp`

- Create a temporary directory in `/tmp/` and print its absolute path:

`mktemp --directory`

- Create an empty temporary file at the specified path, with `X`s replaced with random alphanumeric characters, and print its path:

`mktemp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_XXXXX_name</span>`"`

- Create an empty temporary file in `/tmp/` with the specified name, with `X`s replaced with random alphanumeric characters, and print its path:

`mktemp -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_XXXXX_name</span>`"`
