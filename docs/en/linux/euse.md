---
layout: page
title: linux/euse (English)
description: "Enable, disable, and obtain information about Gentoo USE flags."
content_hash: 9ae2f30e1f36a4a4e9b12579f3c9aec3b0049ca5
last_modified_at: 2024-12-08
tldri18n_status: 2
---
# euse

Enable, disable, and obtain information about Gentoo USE flags.
More information: <https://wiki.gentoo.org/wiki/Euse>.

- List active global USE flags:

`euse --active --global`

- List active local USE flags:

`euse --active --local`

- Enable a global USE flag:

`sudo euse --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">use_flag</span>

- Disable a global USE flag (put a '-' sign in front of the USE flag):

`sudo euse --disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">use_flag</span>

- Remove a global USE flag:

`sudo euse --prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">use_flag</span>
