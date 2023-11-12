---
layout: page
title: linux/edquota (English)
description: "Edit quotas for a user or group. By default it operates on all filesystems with quotas."
content_hash: 546da6f2f31f07d43c665d2c4f7a9a1fc03c8b5c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# edquota

Edit quotas for a user or group. By default it operates on all filesystems with quotas.
Quota information is stored permanently in the `quota.user` and `quota.group` files in the root of the filesystem.
More information: <https://manned.org/edquota>.

- Edit quota of the current user:

`edquota --user $(whoami)`

- Edit quota of a specific user:

`sudo edquota --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Edit quota for a group:

`sudo edquota --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>

- Restrict operations to a given filesystem (by default edquota operates on all filesystems with quotas):

`sudo edquota --file-system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem</span>

- Edit the default grace period:

`sudo edquota -t`

- Duplicate a quota to other users:

`sudo edquota -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reference_user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_user1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_user2</span>
