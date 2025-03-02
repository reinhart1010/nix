---
layout: page
title: linux/steamos-chroot (English)
description: "Switch root directory in a SteamOS environment."
content_hash: 0d53faa9352a9d429a907f1db4fd229e965b1667
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/steamos-chroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# steamos-chroot

Switch root directory in a SteamOS environment.
More information: <https://gitlab.com/users/evlaV/projects>.

- Switch to the other A/B partition:

`steamos-chroot --partset other`

- Switch to a partition on another drive:

`steamos-chroot --disk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>` --partset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|B</span>

- Display help:

`steamos-chroot --help`
