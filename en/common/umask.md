---
layout: page
title: common/umask (English)
description: "Manage the read/write/execute permissions that are masked out (i.e. restricted) for newly created files by the user."
content_hash: a50ea7a610a498fcb6f407acc165fd640d00b4e1
---
# umask

Manage the read/write/execute permissions that are masked out (i.e. restricted) for newly created files by the user.
More information: <https://manned.org/umask>.

- Display the current mask in octal notation:

`umask`

- Display the current mask in symbolic (human-readable) mode:

`umask -S`

- Change the mask symbolically to allow read permission for all users (the rest of the mask bits are unchanged):

`umask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a+r</span>

- Set the mask (using octal) to restrict no permissions for the file's owner, and restrict all permissions for everyone else:

`umask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">077</span>
