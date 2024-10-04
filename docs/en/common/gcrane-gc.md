---
layout: page
title: common/gcrane-gc (English)
description: "List images that are not tagged."
content_hash: 183a7a6ef43d78c1c981485445d90d21d2db7500
last_modified_at: 2024-10-04
tldri18n_status: 2
---
# gcrane gc

List images that are not tagged.
Will calculate images that can be garbage-collected.
This can be composed with `gcrane delete` to actually garbage collect them.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- List untagged images:

`gcrane gc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Whether to recurse through repositories:

`gcrane gc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>

- Display help:

`gcrane gc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
