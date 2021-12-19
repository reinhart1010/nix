---
layout: page
title: common/corepack (English)
description: "Zero-runtime-dependency package acting as bridge between Node projects and their package managers."
content_hash: ec2a036ae79dda3f8a9a80de2d728692ac7e9708
---
# corepack

Zero-runtime-dependency package acting as bridge between Node projects and their package managers.
More information: <https://github.com/nodejs/corepack>.

- Add the Corepack shims to the Node.js installation directory to make them available as global commands:

`corepack enable`

- Add the Corepack shims to a specific directory:

`corepack enable --install-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Remove the Corepack shims from the Node.js installation directory:

`corepack disable`

- Prepare a specific package manager:

`corepack prepare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_manager</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` --activate`

- Prepare the package manager configured for the project in the current path:

`corepack prepare`

- Use a package manager without installing it as a global command:

`corepack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm|pnpm|yarn</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_manager_arguments</span>

- Install a package manager from the specified archive:

`corepack hydrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/corepack.tgz</span>

- Display help for a subcommand:

`corepack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
