---
layout: page
title: common/pnpm (English)
description: "Fast, disk space efficient package manager for Node.js."
content_hash: 675db413a96db424aeae1fb944dfe76ecd3f6d82
---
# pnpm

Fast, disk space efficient package manager for Node.js.
Manage Node.js projects and their module dependencies.
More information: <https://pnpm.io>.

- Create a `package.json` file:

`pnpm init`

- Download all the packages listed as dependencies in `package.json`:

`pnpm install`

- Download a specific version of a package and add it to the list of dependencies in `package.json`:

`pnpm add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Download a package and add it to the list of [D]ev dependencies in `package.json`:

`pnpm add -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Download a package and install it [g]lobally:

`pnpm add -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Uninstall a package and remove it from the list of dependencies in `package.json`:

`pnpm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Print a tree of locally installed modules:

`pnpm list`

- List top-level [g]lobally installed modules:

`pnpm list -g --depth=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
