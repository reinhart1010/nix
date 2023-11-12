---
layout: page
title: common/basenc (English)
description: "Encode or decode file or `stdin` using a specified encoding, to `stdout`."
content_hash: e1454d59dac7edec6c5c74d890ae6082380c1a6f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# basenc

Encode or decode file or `stdin` using a specified encoding, to `stdout`.
More information: <https://www.gnu.org/software/coreutils/basenc>.

- Encode a file with base64 encoding:

`basenc --base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decode a file with base64 encoding:

`basenc --decode --base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Encode from `stdin` with base32 encoding with 42 columns:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | basenc --base32 -w42`

- Encode from `stdin` with base32 encoding:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | basenc --base32`
