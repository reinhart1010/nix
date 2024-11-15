---
layout: page
title: common/npm-ci (English)
description: "Clean install of `npm` project dependencies for automated environments."
content_hash: be919eb9dc7fb22126cfd33e6bf1625d5d8b3736
last_modified_at: 2024-11-15
tldri18n_status: 2
---
# npm ci

Clean install of `npm` project dependencies for automated environments.
Installs packages based on `package-lock.json` or `npm-shrinkwrap.json`.
More information: <https://docs.npmjs.com/cli/commands/npm-ci>.

- Install project dependencies from `package-lock.json` or `npm-shrinkwrap.json`:

`npm ci`

- Install project dependencies but skip the specified dependency type:

`npm ci --omit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev|optional|peer</span>

- Install project dependencies without running any pre-/post-scripts defined in `package.json`:

`npm ci --ignore-scripts`
