---
layout: page
title: linux/eselect-locale (English)
description: "An `eselect` module for managing the `LANG` environment variable, which sets the system language."
content_hash: fd7f650ab56889babe3775568dc07ca4277decbc
last_modified_at: 2024-07-07
tldri18n_status: 2
---
# eselect locale

An `eselect` module for managing the `LANG` environment variable, which sets the system language.
More information: <https://wiki.gentoo.org/wiki/Eselect#Locale>.

- List available locales:

`eselect locale list`

- Set the `LANG` environment variable in `/etc/profile.env` by name or index from the `list` command:

`eselect locale set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|index</span>

- Display the value of `LANG` in `/etc/profile.env`:

`eselect locale show`
