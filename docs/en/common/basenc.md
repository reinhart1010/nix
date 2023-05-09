---
layout: page
title: common/basenc (English)
description: "Encode or decode file or standard input using a specified encoding, to standard output."
content_hash: 495175ff50287491a3f2126c7b36aaceb1150a09
last_modified_at: 2023-05-09
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># basenc

Encode or decode file or standard input using a specified encoding, to standard output.
More information: <https://www.gnu.org/software/coreutils/basenc>.

- Encode a file with base64 encoding:

`basenc --base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decode a file with base64 encoding:

`basenc --decode --base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Encode from `stdin` with base32 encoding with 42 columns:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | basenc --base32 -w42`

- Encode from `stdin` with base32 encoding:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | basenc --base32`
