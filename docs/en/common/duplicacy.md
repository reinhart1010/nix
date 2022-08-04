---
layout: page
title: common/duplicacy (English)
description: "A lock-free deduplication cloud backup tool."
content_hash: 9099aba58ee44cc43cba0e288b0b41f3add17946
---
# duplicacy

A lock-free deduplication cloud backup tool.
More information: <https://github.com/gilbertchen/duplicacy/wiki>.

- Use current directory as the repository, initialize a SFTP storage and encrypt the storage with a password:

`duplicacy init -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sftp://user@192.168.2.100/path/to/storage/</span>

- Save a snapshot of the repository to the default storage:

`duplicacy backup`

- List snapshots of current repository:

`duplicacy list`

- Restore the repository to a previously saved snapshot:

`duplicacy restore -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>

- Check the integrity of snapshots:

`duplicacy check`

- Add another storage to be used for the existing repository:

`duplicacy add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">storage_url</span>

- Prune a specific revision of snapshot:

`duplicacy prune -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>

- Prune revisions, keeping one revision every `n` days for all revisions older than `m` days:

`duplicacy prune -keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n:m</span>
