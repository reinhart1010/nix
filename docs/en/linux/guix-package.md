---
layout: page
title: linux/guix-package (English)
description: "Install, upgrade and remove Guix packages, or rollback to previous configurations."
content_hash: 8c0b1d39ba824467bc351bcdea4ad3a4b0628f68
last_modified_at: 2023-08-26
---
# guix package

Install, upgrade and remove Guix packages, or rollback to previous configurations.
More information: <https://guix.gnu.org/manual/html_node/Invoking-guix-package.html>.

- Install a new package:

`guix package -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package:

`guix package -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search the package database for a regular expression:

`guix package -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- List installed packages:

`guix package -I`

- List generations:

`guix package -l`

- Roll back to the previous generation:

`guix package --roll-back`
