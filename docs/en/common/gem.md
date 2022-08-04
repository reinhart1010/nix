---
layout: page
title: common/gem (English)
description: "Interact with the package manager for the Ruby programming language."
content_hash: 11413e7ed075c4d1237b9ecc570a05b02eef3988
---
# gem

Interact with the package manager for the Ruby programming language.
More information: <https://rubygems.org>.

- Search for remote gem(s) and show all available versions:

`gem search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>` --all`

- Install the latest version of a gem:

`gem install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gemname</span>

- Install specific version of a gem:

`gem install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gemname</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>

- Install the latest matching (SemVer) version of a gem:

`gem install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gemname</span>` --version '~> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>`'`

- Update a gem:

`gem update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gemname</span>

- List all local gems:

`gem list`

- Uninstall a gem:

`gem uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gemname</span>

- Uninstall specific version of a gem:

`gem uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gemname</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>
