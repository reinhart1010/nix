---
layout: page
title: linux/abroot (English)
description: "ABRoot utility provides full immutability and atomicity by transacting between 2 root partition states (A⟺B)."
content_hash: deb41cab4e50da09eac9d84da40d2ecddb4ffc61
last_modified_at: 2022-12-13
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># abroot

ABRoot utility provides full immutability and atomicity by transacting between 2 root partition states (A⟺B).
It also allows on-demand transactions via a transactional shell.
More information: <https://github.com/Vanilla-OS/ABRoot>.

- Output the current or future root partition state:

`sudo abroot get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">present|future</span>

- Enter the transactional shell in the future root partition and switch root on the next boot:

`sudo abroot shell`

- Execute a specific command in the transactional shell in the future root partition and switch to it on the next boot:

`sudo abroot exec "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Install specific packages in the host inside the transactional shell in the future root partition and switch to it on the next boot:

`sudo abroot exec apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Update the boot partition (for advanced users only):

`sudo abroot _update-boot`

- Display help:

`abroot --help`

- Display version:

`abroot --version`
