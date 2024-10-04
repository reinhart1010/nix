---
layout: page
title: linux/eselect-profile (English)
description: "An `eselect` module for managing the `/etc/portage/make.profile` symlink, which sets the system profile."
content_hash: 2203ccf2fe28dfdd94b8089dec320b3c052014d8
last_modified_at: 2024-10-04
tldri18n_status: 2
---
# eselect profile

An `eselect` module for managing the `/etc/portage/make.profile` symlink, which sets the system profile.
More information: <https://wiki.gentoo.org/wiki/Eselect#Profile>.

- List available profile symlink targets with their numbers:

`eselect profile list`

- Set the `/etc/portage/make.profile` symlink by name or number from the `list` command:

`eselect profile set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|number</span>

- Show the current system profile:

`eselect profile show`
