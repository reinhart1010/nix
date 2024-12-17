---
layout: page
title: linux/grub2-mkpasswd-pbkdf2 (English)
description: "Generate a hashed password for GRUB."
content_hash: a56f8b6382fadaa3def9534632bc8355034af370
last_modified_at: 2024-12-17
tldri18n_status: 2
---
# grub2-mkpasswd-pbkdf2

Generate a hashed password for GRUB.
More information: <https://manned.org/grub2-mkpasswd-pbkdf2>.

- Create a password hash for GRUB 2 using PBKDF2 and print it to `stdout`:

`sudo grub2-mkpasswd-pbkdf2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--iteration-count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_pbkdf2_iterations</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--salt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">salt_length</span>
