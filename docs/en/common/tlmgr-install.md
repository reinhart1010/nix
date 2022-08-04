---
layout: page
title: common/tlmgr-install (English)
description: "Install TeX Live packages."
content_hash: 5873703efcb236a30ebf123f0311423f6fb37547
---
# tlmgr install

Install TeX Live packages.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- Install a package and its dependencies:

`sudo tlmgr install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Reinstall a package:

`sudo tlmgr install --reinstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Simulate installing a package without making any changes:

`tlmgr install --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a package without its dependencies:

`sudo tlmgr install --no-depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a package from a specific file:

`sudo tlmgr install --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package</span>
