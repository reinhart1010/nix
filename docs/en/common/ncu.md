---
layout: page
title: common/ncu (English)
description: "Find newer versions of package dependencies and check outdated npm packages locally or globally."
content_hash: 0c5f685b93b394895edeed8c368cf5d5e1f037ff
last_modified_at: 2024-10-20
tldri18n_status: 2
---
# ncu

Find newer versions of package dependencies and check outdated npm packages locally or globally.
`ncu` only updates dependency versions in `package.json`. To install the new versions, run `npm install` afterwards.
More information: <https://github.com/raineorshine/npm-check-updates>.

- List outdated dependencies in the current directory:

`ncu`

- List outdated global `npm` packages:

`ncu --global`

- Upgrade all dependencies in the current directory:

`ncu --upgrade`

- Interactively upgrade dependencies in the current directory:

`ncu --interactive`

- List outdated dependencies up to the highest minor version:

`ncu --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minor</span>

- List outdated dependencies that match a keyword or regular expression:

`ncu --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword|/regex/</span>

- List only a specific section of outdated dependencies:

`ncu --dep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev|optional|peer|prod|packageManager</span>

- Display help:

`ncu --help`
