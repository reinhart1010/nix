---
layout: page
title: common/flow (English)
description: "A static type checker for JavaScript."
content_hash: 32e9ccce924b1d6e835ed4092fbc952490892f49
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# flow

A static type checker for JavaScript.
More information: <https://flow.org>.

- Run a flow check:

`flow`

- Check which files are being checked by flow:

`flow ls`

- Run a type coverage check on all files in a directory:

`flow batch-coverage --show-all --strip-root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display line-by-line type coverage stats:

`flow coverage --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jsx</span>
