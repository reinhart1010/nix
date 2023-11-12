---
layout: page
title: linux/snap (English)
description: "Manage the \"snap\" self-contained software packages."
content_hash: aee55707149cdf82adec1107470f658317aa6998
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/linux/snap.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/snap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snap

Manage the "snap" self-contained software packages.
Similar to what `apt` is for `.deb`.
More information: <https://manned.org/snap>.

- Search for a package:

`snap find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>

- Install a package:

`snap install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Update a package:

`snap refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Update a package to another channel (track, risk, or branch):

`snap refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --channel=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel</span>

- Update all packages:

`snap refresh`

- Display basic information about installed snap software:

`snap list`

- Uninstall a package:

`snap remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Check for recent snap changes in the system:

`snap changes`
