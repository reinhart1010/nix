---
layout: page
title: common/yadm-transcrypt (English)
description: "If `transcrypt` is installed, this command allows you to pass options directly to `transcrypt`."
content_hash: 32b311c6e3afbd678c151d7f43890acecdea10ee
last_modified_at: 2024-10-02
tldri18n_status: 2
---
# yadm-transcrypt

If `transcrypt` is installed, this command allows you to pass options directly to `transcrypt`.
With the environment configured to use the yadm repository.
Transcrypt enables transparent encryption and decryption of files in a Git repository.
More information: <https://github.com/elasticdog/transcrypt>.

- Set the symmetric cipher to utilize for encryption:

`yadm transcrypt --cipher=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cipher</span>

- Pass the password to derive the key from:

`yadm transcrypt --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Assume yes and accept defaults for non-specified options:

`yadm transcrypt --yes`

- Display the current repository's cipher and password:

`yadm transcrypt --display`

- Re -encrypt all encrypted files using new credentials:

`yadm transcrypt --rekey`
