---
layout: page
title: common/gem (English)
description: "A package manager for the Ruby programming language."
content_hash: 6e2ac4046b11b8c525d2b056fbade794799fa31c
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/gem.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/gem.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gem

A package manager for the Ruby programming language.
More information: <https://guides.rubygems.org>.

- Search for remote gem(s) and show all available versions:

`gem search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>` --all`

- Install the latest version of a gem:

`gem install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_name</span>

- Install a specific version of a gem:

`gem install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_name</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>

- Install the latest matching (SemVer) version of a gem:

`gem install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_name</span>` --version '~> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>`'`

- Update a gem:

`gem update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_name</span>

- List all local gems:

`gem list`

- Uninstall a gem:

`gem uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_name</span>

- Uninstall a specific version of a gem:

`gem uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_name</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>
