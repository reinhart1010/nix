---
layout: page
title: linux/paccache (English)
description: "A `pacman` cache cleaning utility."
content_hash: 3f5c3e82d1d1efe4e9bfaa00c5f4b320dc813240
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# paccache

A `pacman` cache cleaning utility.
More information: <https://manned.org/paccache>.

- Remove all but the 3 most recent package versions from the `pacman` cache:

`paccache -r`

- Set the number of package versions to keep:

`paccache -rk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num_versions</span>

- Perform a dry-run and show the number of candidate packages for deletion:

`paccache -d`

- Move candidate packages to a directory instead of deleting them:

`paccache -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
