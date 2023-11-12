---
layout: page
title: common/ncu (English)
description: "Find newer versions of package dependencies and check outdated npm packages locally or globally."
content_hash: f5620ffbc163041ed926478a162c955303dafa72
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ncu

Find newer versions of package dependencies and check outdated npm packages locally or globally.
`ncu` only updates dependency versions in `package.json`. To install the new versions, run `npm install` afterwards.
More information: <https://github.com/raineorshine/npm-check-updates>.

- List outdated dependencies in the current directory:

`ncu`

- List outdated global npm packages:

`ncu -g`

- Upgrade all dependencies in the current directory:

`ncu -u`

- Interactively upgrade dependencies in the current directory:

`ncu -i`

- Display help:

`ncu -h`
