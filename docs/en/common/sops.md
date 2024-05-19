---
layout: page
title: common/sops (English)
description: "SOPS (Secrets OPerationS): a simple and flexible tool for managing secrets."
content_hash: 9f188f333125aca671dad503d18fcae5876019b1
last_modified_at: 2024-05-19
tldri18n_status: 2
---
# sops

SOPS (Secrets OPerationS): a simple and flexible tool for managing secrets.
More information: <https://github.com/mozilla/sops>.

- Encrypt a file:

`sops -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.enc.json</span>

- Decrypt a file to `stdout`:

`sops -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.enc.json</span>

- Update the declared keys in a `sops` file:

`sops updatekeys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.enc.yaml</span>

- Rotate data keys for a `sops` file:

`sops -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.enc.yaml</span>

- Change the extension of the file once encrypted:

`sops -d --input-type json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.enc.json</span>

- Extract keys by naming them, and array elements by numbering them:

`sops -d --extract '["an_array"][1]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.enc.json</span>

- Show the difference between two `sops` files:

`diff <(sops -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret1.enc.yaml</span>`) <(sops -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret2.enc.yaml</span>`)`
