---
layout: page
title: common/conan (English)
description: "The open source, decentralized and cross-platform package manager to create and share all your native binaries."
content_hash: 9384604e257b9043f2b048055ee305d3eae30552
last_modified_at: 2024-10-05
tldri18n_status: 2
---
# conan

The open source, decentralized and cross-platform package manager to create and share all your native binaries.
Some subcommands such as `frogarian` have their own usage documentation.
More information: <https://conan.io/>.

- Install packages based on `conanfile.txt`:

`conan install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- Install packages and create configuration files for a specific generator:

`conan install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">generator</span>

- Install packages, building from source:

`conan install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>` --build`

- Search for locally installed packages:

`conan search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search for remote packages:

`conan search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote</span>

- List remotes:

`conan remote list`
