---
layout: page
title: linux/deborphan (English)
description: "Display orphan packages on operating systems using the APT package manager."
content_hash: 420810b3e85146a3f883a72668e6e064c154cabd
last_modified_at: 2024-09-18
tldri18n_status: 2
---
# deborphan

Display orphan packages on operating systems using the APT package manager.
More information: <https://manned.org/deborphan>.

- Display library packages (from the "libs" section of the package repository) which are not required by another package:

`deborphan`

- List orphan packages from the "libs" section as well as orphan packages that have a name that looks like a library name:

`deborphan --guess-all`

- Find packages which are only recommended or suggested (but not required) by another package:

`deborphan --nice-mode`
