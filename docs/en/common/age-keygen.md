---
layout: page
title: common/age-keygen (English)
description: "Generate `age` key pairs."
content_hash: 2eac7e11e3bde4b7cba6d29cc7e9a0e7b5a60a42
last_modified_at: 2024-02-09
related_topics:
  - title: Indonesia version
    url: /id/common/age-keygen.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/age-keygen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/age-keygen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# age-keygen

Generate `age` key pairs.
See `age` for how to encrypt/decrypt files.
More information: <https://manned.org/age-keygen>.

- Generate a key pair, save it to an unencrypted file, and print the public key to `stdout`:

`age-keygen --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Convert an identit[y] to a recipient and print the public key to `stdout`:

`age-keygen -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
