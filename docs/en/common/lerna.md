---
layout: page
title: common/lerna (English)
description: "Manage JavaScript projects with multiple packages."
content_hash: d5ff8e5ab5640501753ac8d4c20b1377d537b91a
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# lerna

Manage JavaScript projects with multiple packages.
More information: <https://lerna.js.org>.

- Initialize project files (`lerna.json`, `package.json`, `.git`, etc.):

`lerna init`

- Install all external dependencies of each package and symlink together local dependencies:

`lerna bootstrap`

- Run a specific script for every package that contains it in its `package.json`:

`lerna run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script</span>

- Execute an arbitrary shell command in every package:

`lerna exec -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- Publish all packages that have changed since the last release:

`lerna publish`
