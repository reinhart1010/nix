---
layout: page
title: linux/semanage-fcontext (English)
description: "Manage persistent SELinux security context rules on files/directories."
content_hash: 92ff26d6860aad148772c4681912feb97fe808f1
last_modified_at: 2023-08-17
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># semanage fcontext

Manage persistent SELinux security context rules on files/directories.
See also: `semanage`, `restorecon`.
More information: <https://manned.org/semanage-fcontext>.

- List all file labelling rules:

`sudo semanage fcontext --list`

- List all user-defined file labelling rules without headings:

`sudo semanage fcontext --list --locallist --noheading`

- Add a user-defined rule that labels any path which matches a PCRE regex:

`sudo semanage fcontext --add --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">samba_share_t</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'/mnt/share(/.*)?'</span>

- Delete a user-defined rule using its PCRE regex:

`sudo semanage fcontext --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'/mnt/share(/.*)?'</span>

- Relabel a directory recursively by applying the new rules:

`restorecon -R -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
