---
layout: page
title: common/topgrade (English)
description: "Update all applications on the system."
content_hash: 155b34835b751c6d07375ea1e6a6d81d2635fabc
last_modified_at: 2023-11-12
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

- Edit the config file with default editor:

`topgrade --edit-config`
