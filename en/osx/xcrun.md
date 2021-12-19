---
layout: page
title: osx/xcrun (English)
description: "Run or locate development tools and properties."
content_hash: d8db3eee570d8645002bea96bba16885dec9cfe7
---
# xcrun

Run or locate development tools and properties.
More information: <https://www.unix.com/man-page/osx/1/xcrun/>.

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
