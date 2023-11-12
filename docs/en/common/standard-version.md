---
layout: page
title: common/standard-version (English)
description: "Automate versioning and changelog generation, with SemVer and Conventional Commits."
content_hash: e2df90fbb67bdbce84dae0be6ba76d154b5c129b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# standard-version

Automate versioning and changelog generation, with SemVer and Conventional Commits.
More information: <https://github.com/conventional-changelog/standard-version>.

- Update the changelog file and tag a release:

`standard-version`

- Tag a release without bumping the version:

`standard-version --first-release`

- Update the changelog and tag an alpha release:

`standard-version --prerelease alpha`

- Update the changelog and tag a specific release type:

`standard-version --release-as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">major|minor|patch</span>

- Tag a release, preventing hooks from being verified during the commit step:

`standard-version --no-verify`

- Tag a release committing all staged changes, not just files affected by `standard-version`:

`standard-version --commit-all`

- Update a specific changelog file and tag a release:

`standard-version --infile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md</span>

- Display the release that would be performed without performing them:

`standard-version --dry-run`
