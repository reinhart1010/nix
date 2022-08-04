---
layout: page
title: linux/smbpasswd (English)
description: "Add/remove a Samba user or change its password."
content_hash: 6b9cbed3034ee827398eeef8ebcebaaa4229790a
---
# smbpasswd

Add/remove a Samba user or change its password.
Samba users must have an existing local Unix account.
More information: <https://manned.org/smbpasswd.8>.

- Change the current user's SMB password:

`smbpasswd`

- Add a specified user to Samba and set password (user should already exist in system):

`sudo smbpasswd -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Modify an existing Samba user's password:

`sudo smbpasswd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Delete a Samba user (use `pdbedit` instead if the Unix account has been deleted):

`sudo smbpasswd -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
