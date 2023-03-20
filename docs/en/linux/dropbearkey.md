---
layout: page
title: linux/dropbearkey (English)
description: "Generate SSH keys in Dropbear format."
content_hash: 7a270574c79e599361143197b95c1224ea4ecd4b
last_modified_at: 2023-03-20
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dropbearkey

Generate SSH keys in Dropbear format.
More information: <https://manned.org/dropbearkey.1>.

- Generate an SSH key of [t]ype ed25519 and write it to key [f]ile:

`dropbearkey -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ed25519</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key_file</span>

- Generate an SSH key of [t]ype ecdsa and write it to key [f]ile:

`dropbearkey -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ecdsa</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key_file</span>

- Generate an SSH key of [t]ype RSA with 4096-bit key [s]ize and write it to key [f]ile:

`dropbearkey -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key_file</span>

- Print the private key fingerprint and public key in key [f]ile:

`dropbearkey -y -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key_file</span>
