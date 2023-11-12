---
layout: page
title: common/restic (English)
description: "A backup program that aims to be fast, secure and efficient."
content_hash: bd727b35cecaf78d28a0a66386b975abdcda8c8f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# restic

A backup program that aims to be fast, secure and efficient.
More information: <https://restic.net>.

- Initialize a backup repository in the specified local directory:

`restic init --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>

- Backup a directory to the repository:

`restic --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Show backup snapshots currently stored in the repository:

`restic --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` snapshots`

- Restore a specific backup snapshot to a target directory:

`restic --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latest|snapshot_id</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target</span>

- Restore a specific path from a specific backup to a target directory:

`restic --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_id</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target</span>` --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/restore</span>

- Clean up the repository and keep only the most recent snapshot of each unique backup:

`restic forget --keep-last 1 --prune`
