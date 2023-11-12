---
layout: page
title: common/rage (English)
description: "A simple, secure and modern file encryption tool (and Rust library) with small explicit keys, no config options, and UNIX-style composability."
content_hash: 3ecc8d6c0c292a3239751c43081d92535a1a5809
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rage

A simple, secure and modern file encryption tool (and Rust library) with small explicit keys, no config options, and UNIX-style composability.
Rust implementation of `age`.
More information: <https://github.com/str4d/rage>.

- Encrypt a file for `user` and save it to `message.age`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Your secret message</span>`" | rage --encrypt --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/message.age</span>

- Decrypt a file with `identity_file` and save it to `message`:

`rage --decrypt --identity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/identity_file</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>
