---
layout: page
title: osx/xcrun (English)
description: "Run or locate development tools and properties."
content_hash: c9a823fc86d53927b93ee1e0a95751de3cd6613d
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/xcrun.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcrun

Run or locate development tools and properties.
More information: <https://keith.github.io/xcode-man-pages/xcrun.1.html>.

- Find and run a tool from the active developer directory:

`xcrun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tool</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Show verbose output:

`xcrun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tool</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>` --verbose`

- Find a tool for a given SDK:

`xcrun --sdk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_name</span>

- Find a tool for a given toolchain:

`xcrun --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Display help:

`xcrun --help`

- Display version:

`xcrun --version`
