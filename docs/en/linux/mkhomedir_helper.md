---
layout: page
title: linux/mkhomedir_helper (English)
description: "Create the user's home directory after creating the user."
content_hash: bb4169f8b9ef177a4fe543984fce6d044330ca12
last_modified_at: 2023-08-09
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mkhomedir_helper

Create the user's home directory after creating the user.
More information: <https://manned.org/mkhomedir_helper>.

- Create a home directory for a user based on `/etc/skel` with umask 022:

`sudo mkhomedir_helper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Create a home directory for a user based on `/etc/skel` with all permissions for owner (0) and read permission for group (3):

`sudo mkhomedir_helper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">037</span>

- Create a home directory for a user based on a custom skeleton:

`sudo mkhomedir_helper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umask</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/skeleton_directory</span>
