---
layout: page
title: linux/mktemp (English)
description: "Create a temporary file or directory."
content_hash: 50d8699894af766f11cd9847b7d8768c84dee097
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mktemp

Create a temporary file or directory.
More information: <https://www.gnu.org/software/coreutils/mktemp>.

- Create an empty temporary file and print its absolute path:

`mktemp`

- Use a custom directory (defaults to `$TMPDIR`, or `/tmp`):

`mktemp --tmpdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/tempdir</span>

- Use a custom path template (`X`s are replaced with random alphanumeric characters):

`mktemp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/example.XXXXXXXX</span>

- Use a custom file name template:

`mktemp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.XXXXXXXX</span>

- Create an empty temporary file with the given suffix and print its absolute path:

`mktemp --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ext</span>

- Create an empty temporary directory and print its absolute path:

`mktemp --directory`
