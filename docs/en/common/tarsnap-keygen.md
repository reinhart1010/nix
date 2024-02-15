---
layout: page
title: common/tarsnap-keygen (English)
description: "Generate a key file for use with Tarsnap, an online backup service."
content_hash: 955ccc48bcfc4de3456d3ee4ba21b5e8da630c3d
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# tarsnap-keygen

Generate a key file for use with Tarsnap, an online backup service.
More information: <https://www.tarsnap.com/man-tarsnap-keygen.1.html>.

- Register a machine with the Tarsnap server:

`sudo tarsnap-keygen --keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.key</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_email</span>` --machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">machine_name</span>

- Encrypt the key file (a passphrase will be requested twice):

`sudo tarsnap-keygen --keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.key</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_email</span>` --machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">machine_name</span>` --passphrased`
