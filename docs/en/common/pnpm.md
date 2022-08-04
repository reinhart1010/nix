---
layout: page
title: common/pnpm (English)
description: "Fast, disk space efficient package manager for Node.js."
content_hash: 4d4a32dd526392bca99d74a76dda0134e705ea63
---
# pnpm

Fast, disk space efficient package manager for Node.js.
Manage Node.js projects and their module dependencies.
More information: <https://pnpm.io>.

- Interactively create a `package.json` file:

`pnpm init`

- Download all the packages listed as dependencies in `package.json`:

`pnpm install`

- Download a specific version of a package and add it to the list of dependencies in `package.json`:

`pnpm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Download a package and add it to the list of dev dependencies in `package.json`:

`pnpm install --dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Download a package and install it globally:

`pnpm install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Uninstall a package and remove it from the list of dependencies in `package.json`:

`pnpm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Print a tree of locally installed modules:

`pnpm list`

- List top-level [g]lobally installed modules:

`pnpm list -g --depth=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
