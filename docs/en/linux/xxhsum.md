---
layout: page
title: linux/xxhsum (English)
description: "Print or verify checksums using fast non-cryptographic algorithm xxHash."
content_hash: 173e27b10da1f0f5c3e294a159c2750db8afe854
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xxhsum

Print or verify checksums using fast non-cryptographic algorithm xxHash.
More information: <https://github.com/Cyan4973/xxHash>.

- Calculate the checksum for a file using a specific algorithm:

`xxhsum -H`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|32|64|128</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Run benchmark:

`xxhsum -b`
