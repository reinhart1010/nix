---
layout: page
title: linux/chpasswd (English)
description: "Change the passwords for multiple users by using `stdin`."
content_hash: 935520753e20b7ddf0f917ee18b6ba122259bd1d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# chpasswd

Change the passwords for multiple users by using `stdin`.
More information: <https://manned.org/chpasswd.8>.

- Change the password for a specific user:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_password</span>`" | sudo chpasswd`

- Change the passwords for multiple users (The input text must not contain any spaces.):

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username_1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_password_1</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username_2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_password_2</span>`" | sudo chpasswd`

- Change the password for a specific user, and specify it in encrypted form:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_encrypted_password</span>`" | sudo chpasswd --encrypted`

- Change the password for a specific user, and use a specific encryption for the stored password:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_password</span>`" | sudo chpasswd --crypt-method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NONE|DES|MD5|SHA256|SHA512</span>
