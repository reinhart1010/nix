---
layout: page
title: linux/setfacl (English)
description: "Set file access control lists (ACL)."
content_hash: bf359132d854e954e9fdf0d3ed249726e4851c9b
---
# setfacl

Set file access control lists (ACL).

- Modify ACL of a file for user with read and write access:

`setfacl -m u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Modify default ACL of a file for all users:

`setfacl -d -m u::rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Remove ACL of a file for a user:

`setfacl -x u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Remove all ACL entries of a file:

`setfacl -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
