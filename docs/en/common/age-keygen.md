---
layout: page
title: common/age-keygen (English)
description: "Generate `age` key pairs."
content_hash: 7023709e9b5f57ec2744f90d6115b5394cfdf61b
last_modified_at: 2023-12-03
related_topics:
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

- Convert an identity to a recipient and print the public key to `stdout`:

`age-keygen -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
