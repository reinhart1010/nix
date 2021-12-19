---
layout: page
title: linux/smbpasswd (English)
description: "Change a user's SMB password."
content_hash: fefa8ff287e75943cf7803045b97a07383fbbe58
---
# smbpasswd

Change a user's SMB password.
Samba users must also have a local Unix account.

- Change the current user's SMB password:

`smbpasswd`

- Add a specified user to Samba and set password(user should already exist in system):

`smbpasswd -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Modify an existing Samba user's password:

`smbpasswd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Delete a Samba user:

`smbpasswd -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
