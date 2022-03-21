---
layout: page
title: linux/setfacl (English)
description: "Set file access control lists (ACL)."
content_hash: f3cc5bb74eaa2ed4db4d901c847c86033ed10160
---
# setfacl

Set file access control lists (ACL).
More information: <https://manned.org/setfacl>.

- Modify ACL of a file for user with read and write access:

`setfacl -m u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Modify default ACL of a file for all users:

`setfacl -d -m u::rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Remove ACL of a file for a user:

`setfacl -x u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Remove all ACL entries of a file:

`setfacl -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
