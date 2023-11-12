---
layout: page
title: linux/trashy (English)
description: "An alternative to `rm` and `trash-cli` written in Rust."
content_hash: d38e94db116e5973efc6c4e5daa8b9ab2e3f2155
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# trashy

An alternative to `rm` and `trash-cli` written in Rust.
More information: <https://github.com/oberblastmeister/trashy>.

- Move a specific file to the trash:

`trash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Move specific files to the trash:

`trash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- List items in the trash:

`trash list`

- Restore a specific file from the trash:

`trash restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Remove a specific file from the trash:

`trash empty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Restore all files from the trash:

`trash restore --all`

- Remove all files from the trash:

`trash empty --all`
