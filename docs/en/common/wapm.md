---
layout: page
title: common/wapm (English)
description: "The WebAssembly package manager."
content_hash: fbccb11bb94efb797af3d6c52c55a5c77bf46b35
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# wapm

The WebAssembly package manager.
More information: <https://wapm.io/help/reference>.

- Interactively create a new `wapm.toml` file:

`wapm init`

- Download all the packages listed as dependencies in `wapm.toml`:

`wapm install`

- Download a specific version of a package and add it to the list of dependencies in `wapm.toml`:

`wapm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Download a package and install it globally:

`wapm install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Uninstall a package and remove it from the list of dependencies in `wapm.toml`:

`wapm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Print a tree of locally installed dependencies:

`wapm list`

- List top-level globally installed packages:

`wapm list --global`

- Execute a package command using the Wasmer runtime:

`wapm run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>
