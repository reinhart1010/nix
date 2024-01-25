---
layout: page
title: linux/rusnapshot (English)
description: "BTRFS snapshotting utility written in Rust."
content_hash: 4fcb238c2c149bb6cb9122c263707922f0ed98e5
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# rusnapshot

BTRFS snapshotting utility written in Rust.
More information: <https://github.com/Edu4rdSHL/rusnapshot>.

- Create a snapshot using a configuration file:

`sudo rusnapshot --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.toml</span>` --cr`

- List created snapshots:

`sudo rusnapshot -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.toml</span>` --list`

- Delete a snapshot by ID or the name of the snapshot:

`sudo rusnapshot -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.toml</span>` --del --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_id</span>

- Delete all `hourly` snapshots:

`sudo rusnapshot -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.toml</span>` --list --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --clean --kind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hourly</span>

- Create a read-write snapshot:

`sudo rusnapshot -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.toml</span>` --cr --rw`

- Restore a snapshot:

`sudo rusnapshot -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.toml</span>` --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_id</span>` --restore`
