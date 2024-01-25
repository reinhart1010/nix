---
layout: page
title: common/topgrade (English)
description: "Update all applications on the system."
content_hash: 3d767f602808bad8685ba45048ba0edbc5a9ed57
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# topgrade

Update all applications on the system.
More information: <https://github.com/r-darwish/topgrade>.

- Run updates:

`topgrade`

- Say yes to all updates:

`topgrade -y`

- Cleanup temporary/old files:

`topgrade -c`

- Disable a certain update operation:

`topgrade --disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">operation</span>

- Only perform a certain update operation:

`topgrade --only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">operation</span>

- Edit the configuration file with default editor:

`topgrade --edit-config`
