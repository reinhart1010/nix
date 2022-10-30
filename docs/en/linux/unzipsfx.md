---
layout: page
title: linux/unzipsfx (English)
description: "Create a self-extracting compressed binary file by prepending self-extracting stubs on a `zip` file."
content_hash: 44d2ec5d822edd2f0533f838ab8e0163f074fa50
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># unzipsfx

Create a self-extracting compressed binary file by prepending self-extracting stubs on a `zip` file.
More information: <https://manned.org/unzipsfx>.

- Create a self-extracting binary file of a `zip` archive:

`cat unzipsfx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` && chmod 755 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Extract a self-extracting binary in the current directory:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./path/to/binary)</span>

- Test a self-extracting binary for errors:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./path/to/binary)</span>` -t`

- Print content of a file in the self-extracting binary without extraction:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./path/to/binary)</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename</span>

- Print comments on `zip` archive in the self-extracting binary:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./path/to/binary)</span>` -z`
