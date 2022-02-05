---
layout: page
title: common/lerna (English)
description: "A tool for managing JavaScript projects with multiple packages."
content_hash: 98751c6914c8a341e33abde5c6b4a73f9a3790a5
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lerna

A tool for managing JavaScript projects with multiple packages.
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
