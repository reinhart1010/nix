---
layout: page
title: common/npm-version (English)
description: "Bump a node package version."
content_hash: 119838b429da8dddf8120216a1b63eb3d4f12ecb
last_modified_at: 2024-10-31
tldri18n_status: 2
---
# npm version

Bump a node package version.
More information: <https://docs.npmjs.com/cli/commands/npm-version>.

- Check current version:

`npm version`

- Bump the minor version:

`npm version minor`

- Set a specific version:

`npm version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Bump the patch version without creating a Git tag:

`npm version patch --no-git-tag-version`

- Bump the major version with a custom commit message:

`npm version major -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Upgrade to %s for reasons</span>`"`
