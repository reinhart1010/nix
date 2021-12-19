---
layout: page
title: linux/swupd (English)
description: "Package management utility for Clear Linux."
content_hash: 26ae3f373dcd5b3b2a0d86fc636d7af0280a969d
---
# swupd

Package management utility for Clear Linux.
More information: <https://docs.01.org/clearlinux/latest/guides/clear/swupd.html>.

- Update to the latest version:

`sudo swupd update`

- Show current version, and check whether a newer one exists:

`swupd check-update`

- List installed bundles:

`swupd bundle-list`

- Locate the bundle where a wanted package exists:

`swupd search -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a new bundle:

`sudo swupd bundle-add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bundle</span>

- Remove a bundle:

`sudo swupd bundle-remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bundle</span>

- Correct broken or missing files:

`sudo swupd verify`
