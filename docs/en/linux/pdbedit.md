---
layout: page
title: linux/pdbedit (English)
description: "Edit the Samba user database."
content_hash: 2c55f197195ebeb02d5f3c919fd851126e7b4f7b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pdbedit

Edit the Samba user database.
For simple user add/remove/password, you can also use `smbpasswd`.
More information: <https://manned.org/pdbedit>.

- List all Samba users (use verbose flag to show their settings):

`sudo pdbedit --list --verbose`

- Add an existing Unix user to Samba (will prompt for password):

`sudo pdbedit --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --create`

- Remove a Samba user:

`sudo pdbedit --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --delete`

- Reset a Samba user's failed password counter:

`sudo pdbedit --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --bad-password-count-reset`
