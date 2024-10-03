---
layout: page
title: linux/eselect-profile (English)
description: "An `eselect` module for managing the `/etc/portage/make.profile` symlink, which sets the system profile."
content_hash: 2203ccf2fe28dfdd94b8089dec320b3c052014d8
last_modified_at: 2024-10-03
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/eselect-profile.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eselect profile

An `eselect` module for managing the `/etc/portage/make.profile` symlink, which sets the system profile.
More information: <https://wiki.gentoo.org/wiki/Eselect#Profile>.

- List available profile symlink targets with their numbers:

`eselect profile list`

- Set the `/etc/portage/make.profile` symlink by name or number from the `list` command:

`eselect profile set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|number</span>

- Show the current system profile:

`eselect profile show`
