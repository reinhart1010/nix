---
layout: page
title: linux/lchage (English)
description: "Display or change user password policy."
content_hash: 83e7113aaa62a0d0e26d732c160f33fd1ff258ee
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lchage

Display or change user password policy.
More information: <https://manned.org/lchage>.

- Disable password expiration for the user:

`sudo lchage --date -1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Display the password policy for the user:

`sudo lchage --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Require password change for the user a certain number of days after the last password change:

`sudo lchage --maxdays `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_days</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Start warning the user a certain number of days before the password expires:

`sudo lchage --warndays `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_days</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
