---
layout: page
title: common/wapm (English)
description: "The WebAssembly package manager."
content_hash: af9f292ee614636aa63a38ecbda94551fe7a9bf6
---
# wapm

The WebAssembly package manager.
More information: <https://wapm.io/help/reference>.

- Interactively create a new `wapm.toml` file:

`wapm init`

- Download all the packages listed as dependencies in `wapm.toml`:

`wapm install`

- Download a specific version of a package and add it to the list of dependencies in wapm.toml:

`wapm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Download a package and install it globally:

`wapm install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Uninstall a package and remove it from the list of dependencies in `wapm.toml`:

`wapm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Print a tree of locally installed dependencies:

`wapm list`

- List top-level globally installed packages:

`wapm list --global`

- Execute a package command using the Wasmer runtime:

`wapm run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>
