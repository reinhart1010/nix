---
layout: page
title: common/phive (English)
description: "The Phar Installation and Verification Environment for secure PHP application deployment."
content_hash: 2cb005e0cf7b952234fbf970ebae0266b59d7867
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# phive

The Phar Installation and Verification Environment for secure PHP application deployment.
More information: <https://phar.io>.

- Display a list of available aliased Phars:

`phive list`

- Install a specified Phar to the local directory:

`phive install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias|url</span>

- Install a specified Phar globally:

`phive install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias|url</span>` --global`

- Install a specified Phar to a target directory:

`phive install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias|url</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Update all Phar files to the latest version:

`phive update`

- Remove a specified Phar file:

`phive remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias|url</span>

- Remove unused Phar files:

`phive purge`

- List all available commands:

`phive help`
