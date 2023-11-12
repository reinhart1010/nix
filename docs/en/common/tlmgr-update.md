---
layout: page
title: common/tlmgr-update (English)
description: "Update TeX Live packages."
content_hash: c7614285922b8543167af34dc33ba90c7b3e1cd3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tlmgr update

Update TeX Live packages.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- Update all TeX Live packages:

`sudo tlmgr update --all`

- Update tlmgr itself:

`sudo tlmgr update --self`

- Update a specific package:

`sudo tlmgr update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Update all except a specific package:

`sudo tlmgr update --all --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Update all packages, making a backup of the current packages:

`sudo tlmgr update --all --backup`

- Update a specific package without updating its dependencies:

`sudo tlmgr update --no-depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Simulate updating all packages without making any changes:

`sudo tlmgr update --all --dry-run`
