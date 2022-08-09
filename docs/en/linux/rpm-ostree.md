---
layout: page
title: linux/rpm-ostree (English)
description: "A hybrid image/package system."
content_hash: 33e24290a919cb92f228a84696bf2d1ccb28638a
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rpm-ostree

A hybrid image/package system.
Manage ostree deployments, package layers, filesystem overlays, and boot configuration.
More information: <https://coreos.github.io/rpm-ostree/administrator-handbook/>.

- Show rpm-ostree deployments in the order they will appear in the bootloader:

`rpm-ostree status`

- Show packages which are outdated and can be updated:

`rpm-ostree upgrade --preview`

- Prepare a new ostree deployment with upgraded packages and reboot into it:

`rpm-ostree upgrade --reboot`

- Reboot into the previous ostree deployment:

`rpm-ostree rollback --reboot`

- Install a package into a new ostree deployment and reboot into it:

`rpm-ostree install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --reboot`
