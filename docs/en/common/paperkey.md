---
layout: page
title: common/paperkey (English)
description: "An OpenPGP key archiver."
content_hash: 17ce057ccefc75955b93a71f12e9183b02fe6d82
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# paperkey

An OpenPGP key archiver.
More information: <https://www.jabberwocky.com/software/paperkey/>.

- Take a specific secret key and generate a text file with the secret data:

`paperkey --secret-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret_key.gpg</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret_data.txt</span>

- Take the secret key data in `secret_data.txt` and combine it with the public key to reconstruct the secret key:

`paperkey --pubring `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/public_key.gpg</span>` --secrets `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret_data.txt</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_key.gpg</span>

- Export a specific secret key and generate a text file with the secret data:

`gpg --export-secret-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` | paperkey --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret_data.txt</span>
