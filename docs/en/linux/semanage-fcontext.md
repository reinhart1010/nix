---
layout: page
title: linux/semanage-fcontext (English)
description: "Manage persistent SELinux security context rules on files/directories."
content_hash: 315203694ef8744e0a9f616a33313e892ada5813
last_modified_at: 2024-05-27
tldri18n_status: 2
---
# semanage fcontext

Manage persistent SELinux security context rules on files/directories.
See also: `semanage`, `matchpathcon`, `secon`, `chcon`, `restorecon`.
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
