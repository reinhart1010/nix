---
layout: page
title: common/npm-install (English)
description: "Install node packages."
content_hash: 578b844f4b8433bd3112e6a6aea6bf507ef0ab6e
last_modified_at: 2024-10-17
tldri18n_status: 2
---
# npm install

Install node packages.
More information: <https://docs.npmjs.com/cli/commands/npm-install>.

- Install dependencies listed in package.json:

`npm install`

- Download a specific version of a package and add it to the list of dependencies in `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Download the latest version of a package and add it to the list of dev dependencies in `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|--save-dev</span>

- Download the latest version of a package and install it globally:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>
