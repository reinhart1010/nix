---
layout: page
title: linux/setfacl (English)
description: "Set file access control lists (ACL)."
content_hash: 7c35ab2bab2c00350e34df0d4e33ff7ad440914d
last_modified_at: 2024-02-06
tldri18n_status: 2
---
# setfacl

Set file access control lists (ACL).
More information: <https://manned.org/setfacl>.

- [M]odify ACL of a file for user with read and write access:

`setfacl --modify u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- [M]odify [d]efault ACL of a file for all users:

`setfacl --modify --default u::rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Remove ACL of a file for a user:

`setfacl --remove u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Remove all ACL entries of a file:

`setfacl --remove-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
