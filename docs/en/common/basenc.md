---
layout: page
title: common/basenc (English)
description: "Encode or decode file or `stdin` using a specified encoding, to `stdout`."
content_hash: 0ea7a3c45d5a7903f4e745052dd697a370278a29
last_modified_at: 2024-12-10
related_topics:
  - title: 한국어 version
    url: /ko/common/basenc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/basenc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# basenc

Encode or decode file or `stdin` using a specified encoding, to `stdout`.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/basenc-invocation.html>.

- Encode a file with base64 encoding:

`basenc --base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decode a file with base64 encoding:

`basenc --decode --base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Encode from `stdin` with base32 encoding with 42 columns:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | basenc --base32 -w42`

- Encode from `stdin` with base32 encoding:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | basenc --base32`
