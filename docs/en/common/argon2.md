---
layout: page
title: common/argon2 (English)
description: "Calculate Argon2 cryptographic hashes."
content_hash: 223b2e8e4c5c67e1f98d778dcbcd258b853eb9a7
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/argon2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# argon2

Calculate Argon2 cryptographic hashes.
More information: <https://github.com/P-H-C/phc-winner-argon2#command-line-utility>.

- Calculate a hash with a password and a salt with the default parameters:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">salt_text</span>`"`

- Calculate a hash with the specified algorithm:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">salt_text</span>`" -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d|i|id</span>

- Display the output hash without additional information:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">salt_text</span>`" -e`

- Calculate a hash with given iteration [t]imes, [m]emory usage, and [p]arallelism parameters:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">salt_text</span>`" -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>
