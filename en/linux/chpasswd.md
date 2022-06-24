---
layout: page
title: linux/chpasswd (English)
description: "Change the passwords for multiple users by using stdin."
content_hash: ca288285460b0745deb395e88c57231e7326b3f1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chpasswd

Change the passwords for multiple users by using stdin.
More information: <https://manned.org/chpasswd.8>.

- Change the password for a specific user:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_password</span>`" | sudo chpasswd`

- Change the passwords for multiple users (The input text must not contain any spaces.):

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username_1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_password_1</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username_2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_password_2</span>`" | sudo chpasswd`

- Change the password for a specific user, and specify it in encrypted form:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_encrypted_password</span>`" | sudo chpasswd --encrypted`

- Change the password for a specific user, and use a specific encryption for the stored password:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_password</span>`" | sudo chpasswd --crypt-method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NONE|DES|MD5|SHA256|SHA512</span>
