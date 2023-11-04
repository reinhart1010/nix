---
layout: page
title: common/brew-install (English)
description: "Install a Homebrew formula or cask."
content_hash: fafdb7a35195890053060b2d08cd326cb7e8c14e
last_modified_at: 2023-11-04
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># brew install

Install a Homebrew formula or cask.
More information: <https://docs.brew.sh/Manpage#install-options-formulacask->.

- Install a formula/cask:

`brew install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula|cask</span>

- Build and install a formula from source (dependencies will still be installed from bottles):

`brew install --build-from-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Download the manifest, print what would be installed but don't actually install anything:

`brew install --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula|cask</span>
