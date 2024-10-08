---
layout: page
title: linux/apt-clone (English)
description: "Clone/backup/restore the package state of a Debian-based system."
content_hash: 989f20b06056aa13440a9402d691e1d438b11737
last_modified_at: 2024-10-02
tldri18n_status: 2
---
# apt-clone

Clone/backup/restore the package state of a Debian-based system.
More information: <https://github.com/mvo5/apt-clone>.

- Clone the package state of the current system into a specified directory:

`apt-clone clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Create a clone file (`tar.gz`) for backup purposes:

`apt-clone clone --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/backup.tar.gz</span>

- Restore the package state from a clone file:

`apt-clone restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/backup.tar.gz</span>

- Show information about a clone file (e.g., the release, architecture):

`apt-clone info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/backup.tar.gz</span>

- Check if the clone file can be restored on the current system:

`apt-clone restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/backup.tar.gz</span>` --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/restore</span>
