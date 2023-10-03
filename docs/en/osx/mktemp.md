---
layout: page
title: osx/mktemp (English)
description: "Create a temporary file or directory."
content_hash: 1c71becd44b69ae3fa114f7b1b9d875faa1b5445
last_modified_at: 2023-10-03
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mktemp

Create a temporary file or directory.
More information: <https://keith.github.io/xcode-man-pages/mktemp.1.html>.

- Create an empty temporary file and print its absolute path:

`mktemp`

- Use a custom directory (defaults to the output of `getconf DARWIN_USER_TEMP_DIR`, or `/tmp`):

`mktemp --tmpdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/tempdir</span>

- Use a custom path template (`X`s are replaced with random alphanumeric characters):

`mktemp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/example.XXXXXXXX</span>

- Use a custom file name prefix:

`mktemp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example</span>

- Create an empty temporary directory and print its absolute path:

`mktemp --directory`
