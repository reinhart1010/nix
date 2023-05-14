---
layout: page
title: common/makepasswd (English)
description: "Generate and encrypt passwords."
content_hash: e3607b7195d448c740f5200ccb5b57bf7f99675b
last_modified_at: 2023-05-14
---
# makepasswd

Generate and encrypt passwords.
More information: <https://manpages.debian.org/latest/makepasswd/makepasswd.1.en.html>.

- Generate a random password (8 to 10 characters long, containing letters and numbers):

`makepasswd`

- Generate a 10 characters long password:

`makepasswd --chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Generate a 5 to 10 characters long password:

`makepasswd --minchars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` --maxchars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Generate a password containing only the characters "b", "a" or "r":

`makepasswd --string `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>
