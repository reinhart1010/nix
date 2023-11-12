---
layout: page
title: common/mktemp (English)
description: "Create a temporary file or directory."
content_hash: 8c3336bbab0a489e9422de04b693052e7e19f37e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mktemp

Create a temporary file or directory.
More information: <https://man.openbsd.org/mktemp.1>.

- Create an empty temporary file and print its absolute path:

`mktemp`

- Use a custom directory if `$TMPDIR` is not set (the default is platform-dependent, but usually `/tmp`):

`mktemp -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/tempdir</span>

- Use a custom path template (`X`s are replaced with random alphanumeric characters):

`mktemp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/example.XXXXXXXX</span>

- Use a custom file name template:

`mktemp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.XXXXXXXX</span>

- Create an empty temporary directory and print its absolute path:

`mktemp -d`
