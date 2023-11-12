---
layout: page
title: common/tlmgr-remove (English)
description: "Uninstall TeX Live packages."
content_hash: 340c72b298bd8c2c475deb45abb504490fd2686a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tlmgr remove

Uninstall TeX Live packages.
By default, removed packages will be backed up to `./tlpkg/backups` under the TL installation directory.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- Uninstall a TeX Live package:

`sudo tlmgr remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Simulate uninstalling a package without making any changes:

`tlmgr remove --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Uninstall a package without its dependencies:

`sudo tlmgr remove --no-depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Uninstall a package and back it up to a specific directory:

`sudo tlmgr remove --backupdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Uninstall all of TeX Live, asking for confirmation:

`sudo tlmgr remove --all`
