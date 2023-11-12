---
layout: page
title: linux/openrc (English)
description: "The OpenRC service manager."
content_hash: 62729feaed52e38270be6bde46aa040c133f0f3b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# openrc

The OpenRC service manager.
See also `rc-status`, `rc-update`, and `rc-service`.
More information: <https://wiki.gentoo.org/wiki/OpenRC>.

- Change to a specific runlevel:

`sudo openrc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runlevel_name</span>

- Change to a specific runlevel, but don't stop any existing services:

`sudo openrc --no-stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runlevel_name</span>
