---
layout: page
title: common/npm-ci (English)
description: "Clean install of `npm` project dependencies for automated environments."
content_hash: be919eb9dc7fb22126cfd33e6bf1625d5d8b3736
last_modified_at: 2024-11-14
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-ci.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm ci

Clean install of `npm` project dependencies for automated environments.
Installs packages based on `package-lock.json` or `npm-shrinkwrap.json`.
More information: <https://docs.npmjs.com/cli/commands/npm-ci>.

- Install project dependencies from `package-lock.json` or `npm-shrinkwrap.json`:

`npm ci`

- Install project dependencies but skip the specified dependency type:

`npm ci --omit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev|optional|peer</span>

- Install project dependencies without running any pre-/post-scripts defined in `package.json`:

`npm ci --ignore-scripts`
