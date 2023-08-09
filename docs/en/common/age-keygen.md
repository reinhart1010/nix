---
layout: page
title: common/age-keygen (English)
description: "Generate `age` key pairs."
content_hash: 5ade434f53611246b7165ff2d04f55d935344c47
last_modified_at: 2023-08-09
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># age-keygen

Generate `age` key pairs.
See `age` for how to encrypt/decrypt files.
More information: <https://manned.org/age-keygen>.

- Generate a key pair, save it to an unencrypted file and print the public key to `stdout`:

`age-keygen --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Convert an identity to a recipient and print the public key to `stdout`:

`age-keygen -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
