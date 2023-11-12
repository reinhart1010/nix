---
layout: page
title: common/xkcdpass (English)
description: "A flexible and scriptable password generator which generates strong passphrases."
content_hash: e1f19a6756c4aa3c76baaf723561c91f20989c3d
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/common/xkcdpass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xkcdpass

A flexible and scriptable password generator which generates strong passphrases.
Inspired by XKCD 936.
More information: <https://github.com/redacted/XKCD-password-generator>.

- Generate one passphrase with the default options:

`xkcdpass`

- Generate one passphrase whose first letters of each word match the provided argument:

`xkcdpass -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">acrostic</span>

- Generate passwords interactively:

`xkcdpass -i`
