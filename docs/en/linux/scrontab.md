---
layout: page
title: linux/scrontab (English)
description: "Manage Slurm crontab files."
content_hash: 0dec8f4ca27578b64a09109074e541f75e1741be
last_modified_at: 2023-12-19
tldri18n_status: 2
---
# scrontab

Manage Slurm crontab files.
More information: <https://slurm.schedmd.com/scrontab.html>.

- Install a new crontab from the specified file:

`scrontab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- [e]dit the crontab of the current user:

`scrontab -e`

- [e]dit the crontab of the specified user:

`scrontab --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_id</span>` -e`

- [r]emove the current crontab:

`scrontab -r`

- Print the crontab of the current user to `stdout`:

`scrontab -l`
